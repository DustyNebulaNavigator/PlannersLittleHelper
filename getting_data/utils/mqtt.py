from decouple import config
import json
import paho.mqtt.client as mqtt
from typing import Dict


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
        client.subscribe("Advantech/+/data")

    def on_message(self, client, userdata, msg):
        mac_address = msg.topic.split('/')[1]
        
        if mac_address in self.machines.mac_list:
            macine_name = self.machines.mac_list.get(mac_address).get('name')
            timestamp = int(msg.timestamp)
            data = json.loads(msg.payload)
            machine_on = data.get('di1')
            counter = int(data.get('di2'))
            machine_status = data.get('di6')

            # If counter has not changed, pass
            if self.counter_values[macine_name] == counter:
                return None
                
            self.counter_values[macine_name] = counter
            self.db.add_record(machine_name=macine_name, counter=counter, timestamp=timestamp)


        else:
            # Mac address is missing from machines.py file
            print(f"Missing: {mac_address}")
        
    def loop_forever(self):
        self.client.loop_forever()

