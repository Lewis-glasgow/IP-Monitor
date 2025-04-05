
class EntryManager():

    def __init__(self):
        self.Entry_list = [{
            "IP" : "192.168.1.128",
            "Site" : "Site",
            "Radius" : "Radius",
            "Time" : 0,
            "Drops" : 0,
            "State" : 1,
            "Ping" : 0
        }]

    def CreateNewEntry(self, Site, IP, Radius):
        data = {
            "IP" : IP,
            "Site" : Site,
            "Radius" : Radius,
            "Time" : 0,
            "Drops" : 0,
            "State" : 1,
            "Ping" : 0
        }

        self.Entry_list.append(data)

    def DeleteEntry(self, index):
        if len(self.Entry_list) < index+1:
            return False
        
        self.Entry_list.pop(index)
        return True