import time
import requests
import scapy.all as scapy
import os
from dotenv import load_dotenv
from logging import getLogger, INFO
from azure.monitor.opentelemetry import configure_azure_monitor

load_dotenv()
path = os.environ["BACKEND_URL"]
target_ip = os.environ["TARGET_IP"]

configure_azure_monitor()

logger = getLogger(__name__)
logger.setLevel(INFO) # send logs with level at least: info (default: warning)
logger.info("Scanner started")

def display_results(results):
    logger.info("Found {} devices.".format(len(results)))
    print("Found {} devices.".format(len(results)))
    print("IP Address\t\tMAC Address")
    print("-----------------------------------------")
    for result in results:
        print(result["ip"] + "\t\t" + result["mac"])

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    results = []

    for element in answered_list:
        result = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        results.append(result)

    display_results(results)
    
    return results

while 1:
    scan_results = scan(target_ip)    

    for result in scan_results:
        requests.post(
            path+"/devices/heartbeat", 
            data={
                'address':result["mac"],
                'name':result["ip"]
            }
        )

    time.sleep(60)