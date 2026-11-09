import json 
from models import Cab
from val import ValError

def load_cabs():
    with open("cabs.json") as f:
        raw = json.load(f)


        cabs = []
        ids = []

        for item in raw:

            try:
                cab = Cab(item["id"], item["driver"], item["seats"], item["destination"], item["time_slot"])
            except Exception as e:
                raise ValError(f"Invalid cabs.json, {e}")

            if cab.id not in ids:
                cabs.append(cab)
                ids.append(cab.id)
        return cabs