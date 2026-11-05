
class ValError(ValueError):
    pass

def val_slot(value):
    clean = value.strip().lower()
    if clean in ["morning","afternoon","evening","night"]:
            return clean.title()
    else: 
        raise ValError("Invalid Timeslot")

def val_year(value): 
    val_int_in_range(value,1,5)

def val_int_in_range(value,min,max,label=None):
    if not value.isdigit():
        raise ValError(f"Invalid type for {label}")
    if value in range(min,max+1):
        return int(value)
    else:
        raise ValError(f"Invalid Value for {label}")
         

def val_dest(value):
    clean = value.strip().lower()
    if clean in ["delhi","Jaipur"]:
        return str(clean.title())
    else:
         raise ValError("Invalid Destination")

def val_present(value,label): 
    x = value.strip()
    if not x: 
        raise ValError(f"The {label} cannot be empty/null")
    return x 
