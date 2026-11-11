import json,os 
from models import Cab,RideRequest
from val import ValError

CAB_FILE = "cabs.json"
STATE_FILE = "state.json"

def save_state(app):
    data = {
        "next_inc": app.inc,
        "waiting": [r.to_dict() for q in app.waiting.values() for r in q.list()],
        "cabs": [c.to_dict() for c in app.cabs],
    }

    with open(STATE_FILE,"w") as f:
        json.dump(data,f)

def load_state():
    if not os.path.exists(STATE_FILE):
        print("No save file found, starting fresh from cabs.json")
        return None
    try:
        with open(STATE_FILE) as f:
            data = json.load(f)
        cabs = [Cab.from_dict(c) for c in data["cabs"]]
        waiting = [RideRequest.from_dict(r) for r in data["waiting"]]
        next_inc = int(data["next_inc"])
        return cabs, waiting, next_inc
    except Exception as e:
        print(f"Save file is broken ({e})")
        return None

def load_cabs():
    with open(CAB_FILE) as f:
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

