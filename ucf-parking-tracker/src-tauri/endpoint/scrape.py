import requests 
import time

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

for i in data:
    print(i)

