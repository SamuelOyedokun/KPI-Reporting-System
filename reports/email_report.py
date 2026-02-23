import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
from dotenv import load_dotenv
from reports.pdf_report import generate_pdf

load_dotenv()

EMAIL_SENDER   = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# ── Add as many recipients as you want ──────────────────────
# ── Add or remove emails here anytime ──────────────────────
EMAIL_RECEIVERS = [
    os.getenv("EMAIL_RECEIVER"),
    os.getenv("EMAIL_RECEIVER2"),
    os.getenv("EMAIL_RECEIVER3"),
    os.getenv("EMAIL_RECEIVER4"),
    os.getenv("EMAIL_RECEIVER5"),
]
EMAIL_RECEIVERS = [e for e in EMAIL_RECEIVERS if e]

# Remove None values in case .env is missing some
EMAIL_RECEIVERS = [e for e in EMAIL_RECEIVERS if e]

DASHBOARD_URL = "https://kpi-reporting-system-ifxehqzoojyy5g6qcsvob8.streamlit.app/"

def send_kpi_email(pdf_path="data/processed/kpi_report.pdf"):

    # Generate fresh PDF first
    generate_pdf(pdf_path)

    # ── Build Email ─────────────────────────────────────────
    msg = MIMEMultipart()
    msg["From"]    = EMAIL_SENDER
    msg["To"]      = ", ".join(EMAIL_RECEIVERS)
    msg["Subject"] = f"📊 KPI Report — {datetime.now().strftime('%B %d, %Y')}"

    body = f"""
<html><body style="font-family: Arial, sans-serif; color: #333; margin:0; padding:0; background:#f4f6f9;">
<div style="max-width:620px; margin:auto; background:white; border-radius:12px; overflow:hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.08);">

    <!-- Header -->
    <div style="background:#0D1421; padding:36px 40px; text-align:center;">
        <div style="font-size:28px; margin-bottom:6px;">📊</div>
        <h1 style="color:white; margin:0; font-size:22px; font-weight:700; letter-spacing:-0.5px;">
            KPI Summary Report
        </h1>
        <p style="color:#64748B; margin:8px 0 0; font-size:13px;">
            Generated {datetime.now().strftime('%B %d, %Y at %H:%M')}
        </p>
    </div>

    <!-- Blue accent bar -->
    <div style="height:3px; background:linear-gradient(90deg,#63B3ED,#4FD1C5,#F6AD55);"></div>

    <!-- Body -->
    <div style="padding:36px 40px;">
        <p style="font-size:15px; color:#334155; margin-top:0;">Hello,</p>
        <p style="font-size:14px; color:#475569; line-height:1.7;">
            Your automated <strong>KPI Summary Report</strong> for the sales period 
            <strong>2003–2005</strong> is ready. Please find the full PDF report attached 
            to this email.
        </p>

        <!-- Dashboard Button -->
        <div style="text-align:center; margin:28px 0;">
            <a href="{DASHBOARD_URL}" 
               style="background:linear-gradient(135deg,#63B3ED,#4FD1C5);
                      color:white; text-decoration:none; padding:14px 32px;
                      border-radius:8px; font-size:14px; font-weight:600;
                      display:inline-block; letter-spacing:0.3px;">
                🌐 View Live Dashboard
            </a>
        </div>

        <!-- Highlights -->
        <div style="background:#F8FAFC; border-radius:10px; padding:20px 24px; margin-bottom:24px;">
            <h3 style="color:#1E293B; font-size:14px; margin:0 0 14px; text-transform:uppercase; letter-spacing:0.05em;">
                📈 Report Highlights
            </h3>
            <table style="width:100%; border-collapse:collapse;">
                <tr>
                    <td style="padding:8px 0; font-size:13px; color:#475569; border-bottom:1px solid #E2E8F0;">💰 Total Revenue</td>
                    <td style="padding:8px 0; font-size:13px; color:#1E293B; font-weight:600; text-align:right; border-bottom:1px solid #E2E8F0;">$10,032,628.85</td>
                </tr>
                <tr>
                    <td style="padding:8px 0; font-size:13px; color:#475569; border-bottom:1px solid #E2E8F0;">📈 Total Profit</td>
                    <td style="padding:8px 0; font-size:13px; color:#1E293B; font-weight:600; text-align:right; border-bottom:1px solid #E2E8F0;">$4,514,682.98</td>
                </tr>
                <tr>
                    <td style="padding:8px 0; font-size:13px; color:#475569; border-bottom:1px solid #E2E8F0;">📉 Profit Margin</td>
                    <td style="padding:8px 0; font-size:13px; color:#1E293B; font-weight:600; text-align:right; border-bottom:1px solid #E2E8F0;">45.0%</td>
                </tr>
                <tr>
                    <td style="padding:8px 0; font-size:13px; color:#475569; border-bottom:1px solid #E2E8F0;">🏆 Top Product</td>
                    <td style="padding:8px 0; font-size:13px; color:#1E293B; font-weight:600; text-align:right; border-bottom:1px solid #E2E8F0;">Classic Cars</td>
                </tr>
                <tr>
                    <td style="padding:8px 0; font-size:13px; color:#475569; border-bottom:1px solid #E2E8F0;">🌍 Top Region</td>
                    <td style="padding:8px 0; font-size:13px; color:#1E293B; font-weight:600; text-align:right; border-bottom:1px solid #E2E8F0;">USA — $3.6M</td>
                </tr>
                <tr>
                    <td style="padding:8px 0; font-size:13px; color:#475569;">🔁 Retention Rate</td>
                    <td style="padding:8px 0; font-size:13px; color:#1E293B; font-weight:600; text-align:right;">38.1%</td>
                </tr>
            </table>
        </div>

        <!-- Note -->
        <div style="background:#EFF6FF; border-left:4px solid #63B3ED; padding:12px 16px; border-radius:4px;">
            <p style="margin:0; font-size:13px; color:#3B82F6;">
                📎 The complete PDF report with all tables and breakdowns is attached to this email.
            </p>
        </div>
    </div>

    <!-- Footer -->
    <div style="background:#F8FAFC; padding:20px 40px; text-align:center; border-top:1px solid #E2E8F0;">
        <p style="color:#94A3B8; font-size:12px; margin:0;">
            KPI Reporting System &nbsp;·&nbsp; Auto-generated {datetime.now().strftime('%Y-%m-%d %H:%M')}
            &nbsp;·&nbsp; Built by Samuel Oyedokun
        </p>
    </div>

</div>
</body></html>
"""
    msg.attach(MIMEText(body, "html"))

    # ── Attach PDF ──────────────────────────────────────────
    with open(pdf_path, "rb") as f:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition",
                        f"attachment; filename=kpi_report_{datetime.now().strftime('%Y%m%d')}.pdf")
        msg.attach(part)

    # ── Send to All Recipients ──────────────────────────────
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVERS, msg.as_string())
        print(f"✅ Email sent successfully to:")
        for email in EMAIL_RECEIVERS:
            print(f"   → {email}")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

if __name__ == "__main__":
    send_kpi_email()