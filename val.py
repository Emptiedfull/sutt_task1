
class ValError(ValueError):
    pass

def val_slot(value):
    clean = value.strip().lower()
    if clean in ["morning","afternoon","evening","night"]:
            return clean.title()
    else: 
        raise ValError("Invalid Timeslot")

def val_year(value): 
    if value.isdigit(): 
        if value in range(1,6):
            return value
    raise ValError("Invalid Academic Year")
         

def val_dest(value):
    clean = value.strip().lower()
    if clean in ["delhi","Jaipur"]:
        return clean.title()
    else:
         raise ValError("Invalid Destination")

def val_present(value,label): 
    x = value.strip()
    if not x: 
        raise ValError(f"The {label} cannot be empty/null")
    return x 
