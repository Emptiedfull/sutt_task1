# Cab matching service

*This is built for sutt backend recruitments*

This is a command line service for matching people car pooling with available cab services.

## How to run 

```bash
python3 main.py
```

There are no external dependencies/libraries but it must be run from source directory.

## Cab file (`cabs.json`)

All avialable cabs are loaded once during startup from `cabs.json`. Each cab has an ID, a driver, a seat count (1–4), a destination and a time slot:

```json
[
  {"id": "C1", "driver": "Ramesh", "seats": 4, "destination": "Delhi",  "time_slot": "Morning"},
  {"id": "C2", "driver": "Suresh", "seats": 2, "destination": "Delhi",  "time_slot": "Morning"},
  {"id": "C3", "driver": "Mahesh", "seats": 4, "destination": "Jaipur", "time_slot": "Evening"}
]
```

- `destination`: `Delhi` or `Jaipur`
- `time_slot`: `Morning`, `Afternoon`, `Evening` or `Night`
- `seats`: 1 to 4 

Check repository for a sample cabs.json 

## Tricky situations 

### 1. Half empty cab 
As per the spec, a cab can leave with less than the capacity of the cab using both send trip or send cab options. 

### 2. No cabs left
If a request is added which has no corresponding cab available, they are shown a warning for the same. There request still remains waiting in the queue so their request is still tracked and visible. 

### 3. Same year
Each request contains a unique incrementing number, in the queue tuple this is stored in the second position after the students year. Therefore if 2 students are in the same year, this number is compared next. As the request which was made first is lower it will be selected first and given priority. 

