import requests 
import time
import json
from datetime import datetime



URL = "https://secure.parking.ucf.edu/GarageCounter/GetOccupancy"

params = {"": str(int(time.time() * 1000))}

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/115.0.0.0 Safari/537.36 "
        "[UCFParkingTrackerBot/1.0 - github.com/jcolon030/ucf-parking-tracker]"
    )
}

response = requests.get(URL, params=params, headers=headers)
data = response.json()

timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
entry = {'timestamp': timestamp}

for item in data:
    garage_name = item["location"]["name"]
    vacant = item["location"]["counts"]["vacant"]
    occupied = item["location"]["counts"]["occupied"]
    entry[garage_name] = [vacant, occupied]
                          
# Load existing log (or start fresh)
try:
    with open("static/garage_data.json", "r") as f:
        log = json.load(f)
except FileNotFoundError:
    log = []

# Append new entry
log.append(entry)

# Trim to 48 entries (24 hours if scraped every 30 minutes)
log = log[-48:]

# Save back to file
with open(r"ucf-parking-tracker\static\garage_data.json", "a") as f:
    json.dump(log, f, indent=2)
