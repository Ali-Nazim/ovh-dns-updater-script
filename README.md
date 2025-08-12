# OVH Dynamic DNS Updater

This script (`update_dns.py`) automatically updates the A records of your OVH domain to match your current public IP address. It is useful for maintaining up-to-date DNS records when your IP address changes (e.g., on a home internet connection).

## Features

- Fetches your current public IP address.
- Updates all A records for the specified domain if the IP has changed.
- Refreshes the DNS zone after updates.

## Requirements

- Python 3.x
- [ovh](https://pypi.org/project/ovh/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

Install dependencies with:

```bash
pip install ovh requests python-dotenv
```

## Configuration

Create a `.env` file in the same directory with the following variables:

```
OVH_ENDPOINT=ovh-ca
OVH_APPLICATION_KEY=your_app_key
OVH_APPLICATION_SECRET=your_app_secret
OVH_CONSUMER_KEY=your_consumer_key
```

Replace the values with your OVH API credentials.

## Usage

Run the script:

```bash
python update_dns.py
```

The script will:

1. Load your OVH credentials from `.env`.
2. Fetch your current public IP.
3. Update all A records for the domain specified in the script (`DOMAIN_NAME`).
4. Refresh the DNS zone if any records were updated.

## Setup

### 1. Create a Python Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the same directory as the script with the following content:

```
OVH_ENDPOINT=ovh-ca
OVH_APPLICATION_KEY=your_app_key
OVH_APPLICATION_SECRET=your_app_secret
OVH_CONSUMER_KEY=your_consumer_key
```

Replace the placeholder values with your actual OVH API credentials.

### 4. Set Up a Cronjob

To run the script automatically (e.g., every 10 minutes), add a cronjob. Use the full path to your Python venv and script.

Edit the root crontab:

```bash
sudo crontab -e
```

Add a line like this (replace `/home/toshiba/cron-scripts/dns-update/venv` if your venv is elsewhere):

```
*/10 * * * * /home/toshiba/cron-scripts/dns-update/venv/bin/python /home/toshiba/cron-scripts/dns-update/update_dns.py >> /var/log/update_dns.log 2>&1
```

This will run the script every 10 minutes and log output to `/var/log/update_dns.log`.

## Customization

To use a different domain, change the `DOMAIN_NAME` variable in `update_dns.py`.

## Notes

- Make sure your OVH API credentials have sufficient permissions to read and update DNS records.
- You can schedule this script to run periodically using cron for automated updates.

