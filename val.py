
class ValError(ValueError):
    pass

def val_slot(value):
    clean = value.strip().lower()
    if clean in ["morning","afternoon","evening","night"]:
            return clean.title()
    else: 
        raise ValError("Invalid Timeslot")

def val_year(value): 
   
    return val_int_in_range(value,1,5,"year")

def val_int_in_range(value,min,max,label="value"):
    if isinstance(value, bool):
        raise ValError(f"Invalid type for {label}")
    if isinstance(value, int):
        num = value
    elif isinstance(value, str) and value.strip().isdecimal():
        num = int(value.strip())
    else:
        raise ValError(f"Invalid type for {label}")

    if not (min <= num <= max):
        raise ValError(f"{label} must be between {min} and {max}")
    return num


def val_dest(value):
    clean = value.strip().lower()
    if clean in ["delhi","jaipur"]:
        return str(clean.title())
    else:
         raise ValError(f"Invalid Destination,{clean}")

def val_present(value,label = "name"): 
    x = value.strip()
    if not x: 
        raise ValError(f"The {label} cannot be empty/null")
    return x 

