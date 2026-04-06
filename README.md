# 🚀 Serverless CSV Analytics Pipeline (AWS)

## 📌 Overview
This project is a serverless data pipeline built on AWS that automatically processes CSV files uploaded to Amazon S3. The system cleans the data, calculates key business metrics, and generates interactive HTML charts.

---

## 🏗️ Architecture Diagram

```mermaid
flowchart TD
    A[Upload CSV] --> B[S3 Bucket raw/]
    B --> C[Trigger Lambda]
    C --> D[Python Processing]

    D --> E[Cleaned CSV<br/>processed/]
    D --> F[Summary JSON<br/>summary/]
    D --> G[Charts HTML<br/>charts/]

🏗️ Workflow
You upload CSV
      ↓
S3 Bucket (raw/)
      ↓
Lambda triggers automatically
      ↓
Python code runs
      ↓
┌─────────────────────────────┐
│  Cleaned CSV  → processed/  │
│  Summary JSON → summary/    │
│  Charts HTML  → charts/     │
└─────────────────────────────┘
⚙️ Technologies Used
Amazon S3 – File storage
AWS Lambda – Serverless processing
Python – ETL logic
Plotly – HTML charts
IAM – Permissions
CloudWatch – Logging
📂 Project Structure
AmazonLambda/
│── lambda_function.py
│── build.ps1
│── README.md
│── .gitignore

📥 Input

Upload CSV file to:

raw/
Example CSV
order_id,customer_name,product,quantity,price,order_date
1001,Rakesh,Keyboard,2,499,2026-04-01
1002,Anu,Mouse,1,299,2026-04-02

📤 Output
Cleaned Data
processed/cleaned_<filename>.csv
Summary Metrics
summary/summary_<filename>.json
Interactive Charts
charts/sales_by_product.html
charts/sales_by_date.html

📊 Features
Automated ETL pipeline
Event-driven architecture
Data cleaning
KPI calculations
Interactive HTML charts
Fully serverless

🧠 Challenges & Solutions
❌ Matplotlib / NumPy issue

Dependencies built on Windows failed in AWS Lambda (Linux environment).

❌ Kaleido issue

PNG chart generation required heavy dependencies.

❌ Lambda size limit

Deployment exceeded 262 MB.

✅ Final solution
Switched to Plotly HTML charts:
Lightweight
No OS dependency issues
Interactive

🔐 IAM Permissions Required
s3:GetObject
s3:PutObject
s3:ListBucket

🔮 Future Improvements
Add SNS notifications
Use Athena for querying
Build QuickSight dashboard
Add alerts
👨‍💻 Author

Rakesh Malle
Aspiring Data Analyst | AWS | Python | SQL |  AWS

⭐ Project Summary
This project demonstrates:
Serverless ETL
Event-driven AWS design
Real-world cloud debugging
Data analytics pipeline
