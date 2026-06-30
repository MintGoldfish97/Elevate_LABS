# Simple SSH Log Analyzer

A lightweight Python script that scans SSH authentication logs for brute-force login attempts and flags suspicious IP addresses.

## Features

- Parses `auth.log` (or any SSH log) for failed password attempts
- Detects IPs that exceed a failed-login threshold within a configurable time window
- Exports suspicious IPs to `alerts.csv`
- Generates a bar chart (`top_ips.png`) of the top offending IPs

## Requirements

- Python 3.8+
- pandas
- matplotlib

Install dependencies:

```bash
pip install pandas matplotlib
```

## Usage

1. Open `simple_log_ids.py` and edit the configuration section:

```python
LOG_FILE = r"path\to\your\auth.log"   # path to your SSH log
FAILED_THRESHOLD = 5                  # alert if an IP fails this many times...
WINDOW_MINUTES = 5                    # ...within this many minutes
```

2. Run the script:

```bash
python simple_log_ids.py
```

3. Check the output:
   - Console: summary of suspicious IPs
   - `alerts.csv`: detailed list of flagged IPs with attempt counts and timestamps
   - `top_ips.png`: bar chart of the top 10 IPs by failed login count

## Sample Output

```
Parsed 43 matching lines from auth.log

2 suspicious IP(s):
           ip  count               first                last
185.220.101.5      5 2026-06-15 13:00:00 2026-06-15 13:00:17
  45.83.64.12      5 2026-06-15 18:30:00 2026-06-15 18:30:54

Saved to alerts.csv
Chart saved to top_ips.png
```

## How It Works

The script uses a regex to extract timestamps and source IPs from `Failed password` log entries. For each IP, it applies a sliding time-window algorithm: if the number of failed attempts from that IP within any `WINDOW_MINUTES` window reaches `FAILED_THRESHOLD`, the IP is flagged as suspicious. The reported count reflects the IP's total failed attempts across the whole log.
