import json
import requests
from datetime import datetime
from decouple import config
from typing import List, Dict
import urllib3
urllib3.disable_warnings()

from .querystring import QueryString


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
        self.qs = QueryString(self.host)
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
        
    def get_all_work_centers(self):
        select_options = '$select=Id,Number'
        url = f"{self.host}/en/001.1/api/v1/Manufacturing/WorkCenters?{select_options}"
        return  json.loads(requests.get(url, headers=self.headers, verify=False).content)

    
    def get_running_work_intervals(self) -> List[Dict[str, str]]:
        # IsClosedInterval is false, if work interval is ongoing. True if it is finished.
        endpoint = "TimeRecording/WorkIntervals"
        filter_options = {'IsClosedInterval': [0]}
        select_options = ['IsClosedInterval','OperationId']
        url = self.qs.build_url(endpoint=endpoint, select_list=select_options, filter_dict=filter_options)
        response = json.loads(requests.get(url, headers=self.headers, verify=False).content)
        return response
    
    def get_manufacturing_order_operations(self, filter_values: List[str]=None):
        # There are operation rows tahat were created when work order was created.
        # There are not from BOM.
        endpoint = 'Manufacturing/ManufacturingOrderOperations'
        select=['Id','IsClosedInterval','OperationRow','Part', 'WorkCenterId','ReportingEmployeeId']
        expand=['OperationRow', 'Part']
        filter_dict={'Id': filter_values}
        
        url = self.qs.build_url(endpoint=endpoint, expand_list=expand, select_list=select, filter_dict=filter_dict)
        
        response = json.loads(requests.get(url, headers=self.headers, verify=False).content)
        return response