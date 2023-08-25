import paho.mqtt.client as mqtt

from utils.machines import Machines
from utils.db import Database
from utils.mqtt import Mqtt


def main():
    machines = Machines()
    db = Database(machines.names)
    mqtt = Mqtt(machines, db)
    mqtt.loop_forever()


if __name__ == "__main__":
    main()
