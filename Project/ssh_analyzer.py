#!/usr/bin/env python3
"""
Simple SSH Log Analyzer — flags brute-force IPs.
Edit LOG_FILE below, then just run: python simple_log_ids.py
"""

import re
import pandas as pd
import matplotlib.pyplot as plt

# ---- EDIT THESE ----
LOG_FILE = r"E:\pyfiles\ssh log analyzer\auth.log"      # path to your SSH log
FAILED_THRESHOLD = 5        # alerts if an IP fails this many times...
WINDOW_MINUTES = 5          # ...within this many minutes
# ---------------------

SSH_RE = re.compile(r'(?P<time>\w{3}\s+\d+ \d{2}:\d{2}:\d{2}).*Failed password.*from (?P<ip>\d+\.\d+\.\d+\.\d+)')

def parse_log():
    rows = []
    with open(LOG_FILE, errors="ignore") as f:
        for line in f:
            m = SSH_RE.search(line)
            if m:
                ts = pd.to_datetime(f"2026 {m['time']}", format="%Y %b %d %H:%M:%S")
                rows.append((m["ip"], ts))
    return pd.DataFrame(rows, columns=["ip", "time"])

def find_alerts(df):
    alerts = []
    window = pd.Timedelta(minutes=WINDOW_MINUTES)
    for ip, group in df.groupby("ip"):
        times = group["time"].sort_values().tolist()
        i = 0
        for j in range(len(times)):
            while times[j] - times[i] > window:
                i += 1
            if j - i + 1 >= FAILED_THRESHOLD:
                # count = total failed attempts for this IP (matches chart),
                # window is only used to detect/qualify the burst
                alerts.append({"ip": ip, "count": len(times), "first": times[i], "last": times[j]})
                break
    return pd.DataFrame(alerts)

def main():
    df = parse_log()
    print(f"Parsed {len(df)} matching lines from {LOG_FILE}")

    alerts = find_alerts(df)
    if alerts.empty:
        print("No suspicious activity found.")
    else:
        print(f"\n{len(alerts)} suspicious IP(s):")
        print(alerts.to_string(index=False))
        alerts.to_csv("alerts.csv", index=False)
        print("\nSaved to alerts.csv")

    # quick chart: top IPs by failed-login count
    top = df["ip"].value_counts().head(10)
    top.plot(kind="barh", title="Top IPs by Failed SSH Logins")
    plt.xlabel("Failed attempts")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig("top_ips.png")
    print("Chart saved to top_ips.png")

if __name__ == "__main__":
    main()
