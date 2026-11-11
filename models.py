
from val import *
from datetime import datetime

class RideRequest: 
    def __init__(self,name,dest,time_slot,year,inc,timestamp=None):
        self.name = val_present(name)
        self.dest = val_dest(dest)
        self.time_slot = val_slot(time_slot)
        self.year = int(val_year(year))
        self.inc = inc 
        self.timestamp = timestamp or datetime.now().isoformat(timespec="seconds")
        pass

    @classmethod
    def from_dict(r,d):
        return r(d["name"], d["dest"], d["time_slot"], d["year"], d["inc"], d["timestamp"])

    def to_dict(self):
        return {"name":self.name,"dest":self.dest,"time_slot": self.time_slot,"year":self.year,"inc":self.inc,"timestamp":self.timestamp}

    @property
    def trip(self):
        return (self.dest,self.time_slot)

    def __str__(self):
        return f"#{self.inc} {self.name} (Year {self.year}) → {self.dest}, {self.time_slot}"

class Cab: 
    def __init__(self,id,driver,seats,dest,time_slot,departed=False,passengers=None):
        self.id = val_present(id)
        self.driver = val_present(driver)
        self.seats = val_int_in_range(seats,1,4,"seats")
        self.dest = val_dest(dest)
        self.time_slot = val_slot(time_slot)
        self.departed = departed
        self.passengers = list(passengers or [])
        if len(self.passengers) > self.seats:
            raise ValError(f"passenger capacity exceeded, have {len(self.passengers)} max {self.seats}")

    @classmethod 
    def from_dict(c,d):
        passengers = [RideRequest.from_dict(p) for p in d.get("passengers",[])]
        return c(d["id"],d["driver"],d["seats"],d["destination"],d["time_slot"],departed=bool(d.get("departed",False)),passengers=passengers)

    def to_dict(self):
        return {"id": self.id, "driver": self.driver, "seats": self.seats,
                "destination": self.dest, "time_slot": self.time_slot,
                "departed": self.departed,
                "passengers": [p.to_dict() for p in self.passengers]}
   
    def dispatch(self,riders):
        if self.departed:
            raise RuntimeError(f"Cab {self.id} has departed already")
        else:
            self.passengers.extend(riders)
            self.departed = True

    @property
    def trip(self):
            return (self.dest,self.time_slot)

    @property
    def free_seats(self):
        return self.seats - len(self.passengers)

    @property
    def open(self):
        return not self.departed

    def __str__(self):
        stat = "LEFT" if self.departed else "OPEN"
        return (f"[{self.id}] {self.driver:<10} {self.dest}, {self.time_slot:<9} " f"{len(self.passengers)}/{self.seats}  {stat}")