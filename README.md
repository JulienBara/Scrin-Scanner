# Scrin-Scanner

Setup env

```bash
sudo apt update
sudo apt upgrade
sudo apt-get install libbluetooth-dev
```

Install dependencies

```bash
sudo pip install -r requirements.txt
```

Start the scanner

```bash
sudo python scan_wifi.py
```

## To install the service on the raspberry

```bash
sudo cp scan_wifi.service  /lib/systemd/system/scan_wifi.service
sudo systemctl daemon-reload
sudo systemctl enable scan_wifi.service
sudo systemctl start scan_wifi.service
```

## To check the status of the service on the raspberry

```bash
sudo systemctl status scan_wifi.service
```

## To check the logs of the service on the raspberry

```bash
sudo journalctl -u scan_wifi.service
```

## To uninstall the service on the raspberry

```bash
sudo systemctl stop scan_wifi.service
sudo systemctl disable scan_wifi.service
sudo rm /lib/systemd/system/scan_wifi.service
sudo systemctl daemon-reload
```
