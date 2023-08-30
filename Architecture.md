# Architecure
This project currently consists of 3 programs.
- getting_data
- backend
- frontend

This project is using prebuilt system where ADAM-6060 modules are mounted on machines and these sensors send data to MQTT server.
Theres also node-red app, that data in MQTT topic "Advantech/+/data" and modifies it, and sends it back to "dashboard/status/+" topic

### Getting data
Uses paho.mqtt to subscribe to mqtt topics.
1. "Advantech/+/data" Original data from module. This data includes cycle time and timestamp from module. Module does not know current time. The plus sign is modules MAC address.
2. "dashboard/status/+" This includes machine status and machine name. The plus sign is machine name.

This program saves data to Postgres database. Postgres tables are created by Django.


### Backend


### Frontend

