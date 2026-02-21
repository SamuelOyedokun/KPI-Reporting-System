# 📊 Automated KPI Reporting System

A fully automated business intelligence pipeline that extracts real sales data,
calculates KPIs, generates PDF reports, and delivers them via email on a schedule.

## 🔗 Live Dashboard
👉 [View Live Dashboard](https://kpi-reporting-system-ifxehqzoojyy5g6qcsvob8.streamlit.app/)

## 🚀 Features
- **Live Dashboard** — Interactive charts built with Plotly & Streamlit
- **PDF Report Generation** — Professional formatted reports via ReportLab
- **Automated Email Delivery** — Scheduled HTML email reports with PDF attachment
- **KPI Tracking** — Revenue, Profit Margin, CAC, Retention Rate, and more
- **ETL Pipeline** — Extract, Transform, Load architecture using Pandas & SQL Server
- **Job Scheduler** — Fully automated daily report delivery

## 📊 KPIs Tracked
- 💰 Total Revenue & Profit
- 📉 Profit Margin %
- 🧲 Customer Acquisition Cost (CAC)
- 🔁 Customer Retention Rate
- 📦 Revenue by Product Line
- 🌍 Revenue by Country/Region
- 🏆 Top Customer Rankings
- 📅 Monthly Revenue Trends (2003–2005)

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Pandas | Data transformation |
| SQL Server | Production database |
| Plotly & Streamlit | Interactive dashboard |
| ReportLab | PDF generation |
| smtplib | Email automation |
| schedule | Job scheduling |
| pyodbc & SQLAlchemy | Database connectivity |
| python-dotenv | Environment config |

## 📁 Project Structure
```
kpi-reporting-system/
├── etl/
│   ├── extract.py        # Database extraction
│   ├── transform.py      # KPI calculations
│   └── load.py           # Google Sheets sync
├── reports/
│   ├── pdf_report.py     # PDF generation
│   └── email_report.py   # Email delivery
├── dashboard/
│   └── streamlit_app.py  # Live web dashboard
├── scheduler/
│   └── cron_jobs.py      # Automated scheduling
├── data/
│   └── sales_data_sample.csv
├── config/
│   └── config.yaml
├── main.py               # Central menu
└── requirements.txt
```

## ⚙️ Setup Instructions

1. Clone the repo:
```
git clone https://github.com/oyedonsam100/KPI-Reporting-System.git
```
2. Create virtual environment:
```
python -m venv venv
```
3. Activate it:
```
venv\Scripts\Activate.ps1
```
4. Install dependencies:
```
pip install -r requirements.txt
```
5. Create `.env` file with your credentials
6. Run:
```
python main.py
```

## 🔒 Security Note
The `.env` file containing credentials is excluded via `.gitignore`
and is never committed to GitHub.

## 👤 Author
**Samuel Oyedokun**
[GitHub](https://github.com/oyedonsam100)
