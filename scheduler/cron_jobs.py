import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import schedule
import time
from datetime import datetime
from reports.email_report import send_kpi_email

def job():
    print(f"\n🕐 Scheduled job triggered — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    try:
        send_kpi_email()
        print(f"✅ Job complete — next run scheduled\n")
    except Exception as e:
        print(f"❌ Job failed: {e}\n")

# ── Schedule: Every day at 08:00 AM ─────────────────────────
schedule.every().day.at("08:00").do(job)

print("🚀 KPI Scheduler Running on Render")
print(f"📅 Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("📧 Reports scheduled: Daily at 08:00 AM")
print("─" * 45)

# ── Keep alive forever ───────────────────────────────────────
while True:
    schedule.run_pending()
    time.sleep(60)