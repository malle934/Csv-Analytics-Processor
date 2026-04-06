import json
import boto3
import csv
import io
from urllib.parse import unquote_plus
from collections import defaultdict
import plotly.graph_objects as go

s3 = boto3.client("s3")


def generate_charts(sales_by_product, sales_by_date, bucket_name):
    products = list(sales_by_product.keys())
    product_sales = list(sales_by_product.values())

    fig1 = go.Figure(go.Bar(x=products, y=product_sales))
    fig1.update_layout(
        title="Sales by Product",
        xaxis_title="Product",
        yaxis_title="Revenue",
        width=800,
        height=500
    )
    product_chart_path = "/tmp/sales_by_product.html"
    fig1.write_html(product_chart_path)

    dates = sorted(sales_by_date.keys())
    date_sales = [sales_by_date[date] for date in dates]

    fig2 = go.Figure(go.Scatter(x=dates, y=date_sales, mode="lines+markers"))
    fig2.update_layout(
        title="Sales Trend by Date",
        xaxis_title="Date",
        yaxis_title="Revenue",
        width=800,
        height=500
    )
    date_chart_path = "/tmp/sales_by_date.html"
    fig2.write_html(date_chart_path)

    s3.upload_file(product_chart_path, bucket_name, "charts/sales_by_product.html",
                   ExtraArgs={"ContentType": "text/html"})
    s3.upload_file(date_chart_path, bucket_name, "charts/sales_by_date.html",
                   ExtraArgs={"ContentType": "text/html"})


def lambda_handler(event, context):
    try:
        record = event["Records"][0]
        bucket_name = record["s3"]["bucket"]["name"]
        object_key = unquote_plus(record["s3"]["object"]["key"])

        if not object_key.startswith("raw/"):
            return {
                "statusCode": 200,
                "body": json.dumps("Not a raw file. Skipping.")
            }

        response = s3.get_object(Bucket=bucket_name, Key=object_key)
        csv_content = response["Body"].read().decode("utf-8")

        input_buffer = io.StringIO(csv_content)
        reader = csv.DictReader(input_buffer)

        cleaned_rows = []
        sales_by_product = defaultdict(float)
        sales_by_date = defaultdict(float)

        for row in reader:
            if not row["order_id"] or not row["product"] or not row["order_date"]:
                continue

            quantity = row["quantity"].strip() if row["quantity"] else ""
            quantity = int(quantity) if quantity else 1

            price = row["price"].strip() if row["price"] else ""
            price = float(price) if price else 0.0

            total_amount = quantity * price

            cleaned_row = {
                "order_id": row["order_id"].strip(),
                "customer_name": row["customer_name"].strip().title() if row["customer_name"] else "Unknown",
                "product": row["product"].strip(),
                "quantity": quantity,
                "price": price,
                "order_date": row["order_date"].strip(),
                "total_amount": total_amount
            }

            cleaned_rows.append(cleaned_row)
            sales_by_product[cleaned_row["product"]] += total_amount
            sales_by_date[cleaned_row["order_date"]] += total_amount

        if not cleaned_rows:
            return {
                "statusCode": 200,
                "body": json.dumps("No valid data found.")
            }

        total_revenue = sum(row["total_amount"] for row in cleaned_rows)
        total_orders = len(cleaned_rows)
        average_order_value = total_revenue / total_orders if total_orders else 0

        output_buffer = io.StringIO()
        fieldnames = ["order_id", "customer_name", "product", "quantity", "price", "order_date", "total_amount"]
        writer = csv.DictWriter(output_buffer, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cleaned_rows)

        file_name = object_key.split("/")[-1]
        cleaned_key = f"processed/cleaned_{file_name}"
        summary_key = f"summary/summary_{file_name.replace('.csv', '.json')}"

        s3.put_object(
            Bucket=bucket_name,
            Key=cleaned_key,
            Body=output_buffer.getvalue(),
            ContentType="text/csv"
        )

        summary_data = {
            "input_file": object_key,
            "cleaned_file": cleaned_key,
            "total_orders": total_orders,
            "total_revenue": total_revenue,
            "average_order_value": average_order_value,
            "sales_by_product": dict(sales_by_product),
            "sales_by_date": dict(sales_by_date)
        }

        s3.put_object(
            Bucket=bucket_name,
            Key=summary_key,
            Body=json.dumps(summary_data, indent=2),
            ContentType="application/json"
        )

        generate_charts(sales_by_product, sales_by_date, bucket_name)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "File processed successfully",
                "cleaned_file": cleaned_key,
                "summary_file": summary_key,
                "charts": [
                    "charts/sales_by_product.html",
                    "charts/sales_by_date.html"
                ],
                "total_orders": total_orders,
                "total_revenue": total_revenue,
                "average_order_value": average_order_value
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps(f"Error: {str(e)}")
        }