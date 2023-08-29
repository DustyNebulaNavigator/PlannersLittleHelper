from decouple import config
import json
import paho.mqtt.client as mqtt
from typing import Dict
import re


MQTT_IP = config('MQTT_IP')
MQTT_PORT = int(config('MQTT_PORT'))
MQTT_KEEP_ALIVE = int(config('MQTT_KEEP_ALIVE'))

class Mqtt:
    def __init__(self, machines, db):
        #conn = sqlite3.connect(db_name)
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(MQTT_IP, MQTT_PORT, MQTT_KEEP_ALIVE)
        self.machines = machines
        self.db = db
        self.counter_values = self.get_counter_values()
    
    def get_counter_values(self) -> Dict[str, int]:
        """
        Returns:
            Dict[str, int]: A dictionary with machine name as key and counter value as value.
        """
        counter_values = {}
        for machine in self.machines.names:
            counter_values[machine] = self.db.get_latest_counter_value(machine)
        return counter_values

        
    def on_connect(self, client, userdata, flags, rc):
        client.subscribe([("dashboard/status/+", 0), ("Advantech/+/data", 0)])

    def on_message(self, client, userdata, msg):
        cycle_time_pattern = re.compile(r'^Advantech/([^/]+)/data$')
        status_pattern = re.compile(r'^dashboard/status/([^/]+)$')

        if cycle_time_pattern.match(msg.topic):
            mac_address = msg.topic.split('/')[1]
            
            if mac_address in self.machines.mac_list:
                # Handles cycle time change topic
                macine_name = self.machines.mac_list.get(mac_address).get('name')
                timestamp = int(msg.timestamp)
                data = json.loads(msg.payload)
                machine_on = data.get('di1')
                counter = int(data.get('di2'))
                machine_status = data.get('di6')

                # If counter has not changed, pass
                if self.counter_values[macine_name] != counter:                   
                    self.counter_values[macine_name] = counter
                    self.db.add_record(machine_name=macine_name, counter=counter, timestamp=timestamp)
        
        if status_pattern.match(msg.topic):
            # Handles status change topic
            machine_name = msg.topic.split('/')[2]
            byte_data = msg.payload
            status = byte_data.decode('utf-8')
            self.db.update_machine_status(machine_name, status)
        
    def loop_forever(self):
        self.client.loop_forever()

