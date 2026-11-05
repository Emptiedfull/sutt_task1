from models import Cab,RideRequest 
from val import ValError,val_present,val_dest,val_slot,val_year

def prompt(q,val):
    while True: 
        raw = input(q)
        try:
            return val(raw)
        except ValError as err:
            print(f"{err}")

class App:
    def __init__(self):
        self.cabs = []
        self.waiting = []
        self.inc = 1
        pass

    def add_request(self):
        name = prompt("Name: ",val_present)
        dest = prompt("Destination Delhi/Jaipur): ",val_dest)
        slot = prompt("Timeslot (Morning/Afternoon/Evening/Night): ",val_slot)
        year = prompt("Year (1-5):",val_year)

        req = RideRequest(name,dest,slot,year,self.inc)
        self.inc += 1
        self.waiting.append(req)

        print(f"added {req}")

    def show_status(self):
        print("-> Waiting")
        if not self.waiting:
            print("None")
        for r in self.waiting:
            print(" ",r)

    def menu_ops(self):
        return [
            ("Request Ride", self.add_request),
            ("View Queue", self.show_status),
        ]

    def run(self):
         opts = self.menu_ops()
        
                    print(" ---Welcome---- ")
        
                    for i,(label,_) in enumerate(opts,1):
                        print(f"{i}. {label}")
                    quit_num = i + 1
                    print(f"\n{quit_num}. Quit \n")
        while True:
           

            choice = input("> ").strip()

            try: 
                choice = int(choice)


            if choice == quit_num:
                print("Quitting")
                return

            if choice.isdigit() and 1 <= int(choice) <=  

App().run()
            