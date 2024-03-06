import bluetooth
import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()
path = os.environ["BACKEND_URL"]

while 1:
    nearby_devices = bluetooth.discover_devices(lookup_names=True, duration=30)
    print("Found {} devices.".format(len(nearby_devices)))

    for addr, name in nearby_devices:
        print("  {} - {}".format(addr, name))
        requests.post(
            path+"/devices/heartbeat", 
            data={
                'address':addr,
                'name':name
            }
        )

    time.sleep(60)
