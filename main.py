
from val import *
from datetime import datetime

class RideRequest: 
    def __init__(self,name,dest,time_slot,year,inc,timestamp=None):
        self.name = val_present(name)
        self.dest = val_dest(dest)
        self.time_slot = val_slot(time_slot)
        self.year = val_year(year)
        self.inc = inc 
        self.timestamp = timestamp or datetime.now().isoformat(timespec="seconds")
        pass

class Cab: 
    def __init__(self,id,driver,seats,dest,time_slot,departed=False,passengers=None):
        pass