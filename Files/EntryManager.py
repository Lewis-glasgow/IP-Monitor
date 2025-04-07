
from datetime import datetime
from Files.Serialization import Load

class EntryManager():

    def __init__(self):
        self.Entry_list = Load()

    def CreateNewEntry(self, Site, IP, Radius):
        data = {
            "IP" : IP,
            "Site" : Site,
            "Radius" : Radius,
            "Time" : 0,
            "Drops" : 0,
            "State" : 1,
            "Ping" : 0,
            "Sessions" : {
                "Up" : [datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
                "Down" : []
            }
        }

        self.Entry_list.append(data)

    def DeleteEntry(self, index):
        if len(self.Entry_list) < index+1:
            return False
        
        self.Entry_list.pop(index)
        return True