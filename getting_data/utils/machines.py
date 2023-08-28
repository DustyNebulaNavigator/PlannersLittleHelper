class Machines:
    def __init__(self):
        self.inputs = ["di0", "di6", "di7"]
        self.inputs2 = ["di0", "di2", "di6", "di7"]
        self.mac_list = {
            "74FE48563091":{"name": "M0153", "inputs": self.inputs},
            "74FE485631CD":{"name": "M0083", "inputs": self.inputs2},
            "74FE4858F407":{"name": "M0082", "inputs": self.inputs},
            "74FE4858F408":{"name": "M0081", "inputs": self.inputs},
            "74FE4858F411":{"name": "M0151", "inputs": self.inputs},
            "74FE4858F418":{"name": "M0041", "inputs": self.inputs},
            "74FE4858F6BD":{"name": "M0301", "inputs": self.inputs},
            "74FE4858F6C5":{"name": "M0122", "inputs": self.inputs},
            "74FE485A084B":{"name": "M0052", "inputs": self.inputs},
            "74FE485A0850":{"name": "M0451", "inputs": self.inputs},
            "74FE485A0860":{"name": "M0084", "inputs": self.inputs},
            "74FE485A086B":{"name": "M0044", "inputs": self.inputs},
            "74FE485A0871":{"name": "M0054", "inputs": self.inputs},
            "74FE485A08BC":{"name": "M0422", "inputs": self.inputs},
            "74FE485A0B71":{"name": "M0055", "inputs": self.inputs},
            "74FE485A0B77":{"name": "M0253", "inputs": self.inputs},
            "74FE485A0B93":{"name": "M0056", "inputs": self.inputs},
            "74FE485A1461":{"name": "M1003", "inputs": self.inputs},
            "74FE485A1464":{"name": "M0281", "inputs": self.inputs},
            "74FE485A146C":{"name": "M0091", "inputs": self.inputs},
            "74FE485A146D":{"name": "M0273", "inputs": self.inputs},
            "74FE485A1470":{"name": "M0102", "inputs": self.inputs},
            "74FE485A1477":{"name": "M0501", "inputs": self.inputs},
            "74FE485A147F":{"name": "M0057", "inputs": self.inputs},
            "74FE485A1480":{"name": "M0202", "inputs": self.inputs},
            "74FE485A1482":{"name": "M1002", "inputs": self.inputs},
            "74FE485A1484":{"name": "M0221", "inputs": self.inputs},
            "74FE485A1485":{"name": "M0352", "inputs": self.inputs},
            "74FE485A1487":{"name": "M0402", "inputs": self.inputs},
            "74FE485A1489":{"name": "M0402", "inputs": self.inputs},
            "74FE485A1489":{"name": "M0901", "inputs": self.inputs},
            "74FE4858F6BE":{"name": "M0051", "inputs": self.inputs},
            "74FE485A1E2F":{"name": "M0025", "inputs": self.inputs},
            "74FE485A145E":{"name": "M0123", "inputs": self.inputs},
            "74FE485A147B":{"name": "M0042", "inputs": self.inputs},
            "74FE4858F40E":{"name": "M0101", "inputs": self.inputs},
            "74FE485A0B6F":{"name": "M0201", "inputs": self.inputs},
            "74FE4858F6BC":{"name": "M0121", "inputs": self.inputs},
            "74FE485A1479":{"name": "M0222", "inputs": self.inputs},
            "74FE485A087E":{"name": "M0131", "inputs": self.inputs},
            "74FE486A1E2F":{"name": "OTSI", "inputs": self.inputs}
            
        }
        self.names = [machine.get('name')  for machine in self.mac_list.values()]