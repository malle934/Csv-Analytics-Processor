# 🚀 Serverless CSV Analytics Pipeline (AWS)

## 📌 Project Overview
This project demonstrates a **serverless data analytics pipeline** using AWS. When a CSV file is uploaded to Amazon S3, AWS Lambda is automatically triggered to process the data, generate insights, and create interactive HTML charts.

This project highlights real-world **ETL processing, event-driven architecture, and cloud-based analytics**.

---

## 🏗️ Architecture

User uploads CSV
      ↓
S3 Bucket (raw/)
      ↓
S3 Event Trigger
      ↓
AWS Lambda (Python Processing)
      ↓
Outputs stored in S3:
   - processed/ (Cleaned CSV)
   - summary/ (JSON metrics)
   - charts/ (HTML charts)

---

## 🔐 Key Features

- ✅ Fully serverless architecture  
- ✅ Event-driven processing using S3 triggers  
- ✅ Automated ETL pipeline  
- ✅ Data cleaning and transformation  
- ✅ KPI generation (Revenue, Orders, Average Value)  
- ✅ Interactive HTML charts using Plotly  
- ✅ Scalable and cost-efficient  

---

## 🛠️ Technologies Used

- AWS S3 (Storage)
- AWS Lambda (Compute)
- Python (Data Processing)
- Plotly (Visualization)
- IAM (Access Control)
- CloudWatch (Logging & Debugging)

---

## 📂 Project Workflow

1. Upload CSV file to `raw/` folder in S3  
2. S3 triggers Lambda function  
3. Lambda processes data using Python  
4. Outputs are generated and stored in S3:
   - Cleaned data → `processed/`
   - Summary metrics → `summary/`
   - Charts → `charts/`  

---

## 📊 Sample Output

- 📁 `processed/cleaned_file.csv`
- 📁 `summary/summary.json`
- 📁 `charts/sales_by_product.html`
- 📁 `charts/sales_by_date.html`

---

## 📸 Screenshots (Optional)

![Architecture](architecture.png)
![Output](output.png)

---

## 📚 What I Learned

- Building serverless ETL pipelines using AWS  
- Event-driven architecture with S3 and Lambda  
- Handling AWS Lambda deployment challenges  
- Debugging IAM permission issues  
- Solving dependency and package size limits  
- Generating visualizations in a serverless environment  
- Git & GitHub workflow for project management  

---

## ⚡ Challenges & Solutions

- ❌ Matplotlib & NumPy compatibility issues (Windows vs Lambda Linux)  
- ❌ Kaleido dependency caused large package size  
- ❌ Lambda size limit exceeded (262 MB)  

### ✅ Final Solution
- Switched to **Plotly HTML charts**
- Reduced deployment size  
- Avoided OS compatibility issues  
- Enabled interactive visualizations  

---

## 🔮 Future Improvements

- Add SNS notifications after processing  
- Integrate Athena for querying  
- Build dashboard using QuickSight  
- Add CloudWatch alerts  

---

## 👨‍💻 Author

**Rakesh Malle**  
Aspiring Data Analyst | AWS | Python | SQL | AI  

---

## ⭐ If you like this project
Give it a star ⭐ on GitHub!
