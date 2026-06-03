# 📊 DataVault AI

🚀 **Live Demo**
[https://YOUR-STREAMLIT-APP-URL.streamlit.app](https://datavault-ai-jv2tnstbectwjq7vsej2q8.streamlit.app/)

DataVault AI is an AI-powered Business Intelligence platform built with Python and Streamlit. It automatically detects business datasets, generates executive dashboards, creates forecasting analytics, produces AI-driven insights, and exports professional business reports.

---

## 🚀 Features

### 🔍 Automatic Dataset Detection

DataVault AI automatically identifies:

* Sales Datasets
* Invoice Datasets
* Lead Datasets

---

### 📈 Sales Analytics

* Revenue Analysis
* Profit Analysis
* Orders Analysis
* Margin Calculation
* Revenue by Region
* Top Products Analysis
* Profit by Category
* Revenue Forecasting

---

### 🧾 Invoice Analytics

* Invoice Count
* Vendor Analysis
* Total Spend Tracking
* Spend by Vendor Dashboard

---

### 🎯 Lead Analytics

* Company Analysis
* City Analysis
* Email Analysis
* Lead Distribution Dashboard

---

### 🏢 Executive Dashboard

Executive-level KPIs including:

* Revenue
* Profit
* Orders
* Vendors
* Invoices
* Companies
* Leads

---

### 🤖 AI Insights

Automatically generates business insights such as:

* Top Revenue Region
* Best Performing Products
* Highest Spending Vendors
* Lead Concentration Analysis
* Business Recommendations

---

### 🔮 Forecasting

Machine Learning powered forecasting using Scikit-Learn:

* Revenue Forecasting
* Trend Analysis
* Future Business Projections

---

### 📤 Export Options

* CSV Export
* Excel Export

---

## 📂 Sample Datasets

The repository includes sample datasets for testing:

* `sample_sales_250.xlsx`
* `sample_invoice_250.xlsx`
* `sample_leads_250.csv`

These files are located inside:

```text
sample_data/
```

Users may also upload their own CSV or XLSX files that follow the supported dataset structure.

---

## 📊 Supported Dataset Formats

### Sales Dataset

Required columns:

```text
Date
Product
Category
Region
Revenue
Profit
Quantity
```

### Invoice Dataset

Required columns:

```text
Invoice Number
Vendor
Subtotal
Tax
Total
```

### Lead Dataset

Required columns:

```text
Company
Email
Phone
City
```

---

## 🛠 Technology Stack

* Python
* Streamlit
* Pandas
* Plotly
* NumPy
* Scikit-Learn
* OpenPyXL
* PyMuPDF

---

## 📁 Project Structure

```text
datavault-ai/

├── app/
│   ├── analytics.py
│   ├── data_loader.py
│   ├── executive_dashboard.py
│   ├── exporter.py
│   ├── file_detector.py
│   ├── forecast.py
│   ├── insights.py
│   ├── invoice_analyzer.py
│   ├── lead_analyzer.py
│   ├── sales_analyzer.py
│   └── __init__.py
│
├── dashboard/
│   └── streamlit_app.py
│
├── sample_data/
│   ├── sample_sales_250.xlsx
│   ├── sample_invoice_250.xlsx
│   └── sample_leads_250.csv
│
├── requirements.txt
├── main.py
└── .gitignore
```

---

## ▶️ Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run dashboard/streamlit_app.py
```

---

## 📈 Key Capabilities

* Business Intelligence
* Executive Dashboards
* Forecasting
* Data Analytics
* Financial Analysis
* Lead Analytics
* AI Insights
* Automated Reporting
* CSV & Excel Export

---

## 🔮 Future Enhancements

* PDF Invoice Processing
* Multi-file Upload Support
* Advanced Forecasting Models
* Database Integration
* Authentication & User Management
* Natural Language Business Insights

---

## 👨‍💻 Author

**Biruhi Tesfaye Abeje**

Built as a portfolio project showcasing:

* Python Development
* Streamlit Applications
* Business Intelligence
* Data Analytics
* Forecasting
* Dashboard Development
* Automation Solutions
