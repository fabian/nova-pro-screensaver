# Screensaver for SteelSeries Arctis Nova Pro Wireless

Turn OLED screen of base station black when headphones are not connected.

## Installation

```
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

## Cron

```
*/10 * * * * /Users/YOUR_USER_NAME/Developer/nova-pro-screensaver/.env/bin/python /Users/YOUR_USER_NAME/Developer/nova-pro-screensaver/screensaver.py
```
