from models import Cab,RideRequest 
from val import ValError,val_present,val_dest,val_slot,val_year
from loader import load_cabs
from collections import defaultdict
from queue import Ride_queue as Queue

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
        self.waiting = defaultdict(Queue)
        self.inc = 1
        pass

    

    def add_request(self):
        name = prompt("Name: ",val_present)
        dest = prompt("Destination (Delhi/Jaipur): ",val_dest)
        slot = prompt("Timeslot (Morning/Afternoon/Evening/Night): ",val_slot)
        year = prompt("Year (1-5):",val_year)


        req = RideRequest(name,dest,slot,year,self.inc)
        self.inc += 1
        # self.waiting.append(req)
        self.waiting[req.trip].push(req)



        print(f"added {req}")

    def show_status(self):
        print("-> Waiting")

        for trip,queue in self.waiting.items():
           
            print(f" {trip[0]},{trip[1]} ({len(queue)} waiting)")
            for pos, r in enumerate(queue.list(), 1):
                    print(f"    {pos}. {r}")
       
        print("-> Cabs")
        if not self.cabs:
            print("None")
        for cab in self.cabs:
            print(" ",cab)

    def match_preview(self):
        open_cabs = [c for c in self.cabs if c.open]
        if not open_cabs:
            print("NO OPEN CABS")
            return

        taken = defaultdict(int)

        for cab in open_cabs:
            queue = self.waiting.get(cab.trip)
            start = taken[cab.trip]
            riders = queue.preview(start + cab.free_seats)[start:] if queue else []
            taken[cab.trip] += len(riders)

            print(f"  {cab}")

            if riders:
                for r in riders:
                    print(f"      would take: {r}")
            else: 
                print(f"      no waiting")

    def force_send(self):
        open_cabs = {c.id.lower(): c for c in self.cabs if c.open}
        if not open_cabs:
                   print("NO OPEN CABS")
                   return

        print("-> OPEN CABS")
        for c in open_cabs.values():
            print(" ",c)

        def pick(raw):
            cab = open_cabs.get(raw.strip().lower())
            if cab is None:
                raise ValError(f"No open cab with id {raw}")
            return cab

        cab = prompt("Select cab id: ", pick)
        if cab:
           self.dispatch_cab(cab)


       

    def dispatch_cab(self,cab):
        queue = self.waiting.get(cab.trip)
        riders = queue.pop(cab.free_seats) if queue else []
        cab.dispatch(riders)

        print(f" Cab {cab.id} ({cab.driver}) left for {cab.dest} ")

    def menu_ops(self):
        return [
            ("Request Ride", self.add_request),
            ("View Queue", self.show_status),
            ["Match cabs",self.match_preview],
            ["Send cab",self.force_send]
        ]

    def run(self):
        self.cabs = load_cabs()
        opts = self.menu_ops()
        
        print(" ---Welcome---- ")
        
        for i,(label,_) in enumerate(opts,1):
            print(f"{i}. {label}")
        quit_num = i + 1
        print(f"\n{quit_num}. Quit \n")

        while True:
           

            choice = input("> ").strip()

            if not choice.isdigit():
                print("Please enter a number")
                continue

            choice = int(choice)

            if choice == quit_num:
                print("Quitting")
                return

            if 1 <= int(choice) <=  len(opts):
                opts[choice - 1][1]()
            else:
                print("Please choose a valid menu option")
                continue
                 


App().run()
            