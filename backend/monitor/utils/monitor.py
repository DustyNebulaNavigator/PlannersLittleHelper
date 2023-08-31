import json
import requests
from datetime import datetime
from decouple import config
from typing import List, Dict


import urllib3
urllib3.disable_warnings()

MONITOR_HOST = config("MONITOR_HOST")
MONITOR_USER = config("MONITOR_USER")
MONITOR_PASS = config("MONITOR_PASS")


class Monitor:
    def __init__(self):
        self.username = MONITOR_USER
        self.password = MONITOR_PASS
        self.host = f"https://{MONITOR_HOST}"
        self.headers = {
            "Host": MONITOR_HOST,
            "Content-Type": "application/json",
            "Cache-Control": "no-cache",
            "Accept": "application/json",
            'Connection': 'keep-alive'
        }
        self.login()
        
    def login(self):
        body = {
            "Username": self.username,
            "Password": self.password,
            "ForceRelogin": True
        }
        login_url = f"{self.host}/en/001.1/login"
        login_response = requests.post(
            login_url,
            data=json.dumps(body),
            headers=self.headers,
            verify=False
        )
        # Update Header with session Id
        self.headers["X-Monitor-SessionId"] = login_response.headers["X-Monitor-SessionId"]
    
    def get_part_name_based_on_id(self, part_id: str) -> List[Dict[str, str]]:
        select_options = '$select=Id,PartNumber,Description'
        filter_options = f"$filter=(Id eq '{part_id}')"
        url = f"{self.host}/en/001.1/api/v1/Inventory/Parts?{select_options}&{filter_options}"

        return  json.loads(requests.get(url, headers=self.headers, verify=False).content)
        
