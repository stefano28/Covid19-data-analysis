import json 
  
def write_json(data, filename='AppData/slope.json'): 
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4) 
      
def update(date, slope_ic, ins_ic, slope_h, ins_h):
    with open('AppData/slope.json') as json_file: 
        data = json.load(json_file) 
        n = len(data) - 1
        if(n != -1):
            last = data[n]
            if(date == last['date']):
                return
        temp = data
        y = {
            "date": date, 
            "slope_ic": slope_ic,
            "ins_ic": ins_ic,
            "slope_h": slope_h,
            "ins_h": ins_h
        } 
    
        temp.append(y) 
        
    write_json(data)

def restore():
    with open('AppData/slope.json','w') as f:
        tmp = []
        json.dump(tmp,f)

def write_sat(saturations):
    f = open("AppData/saturations.txt", "w")
    f.write("Name, Value\n")
    for i in saturations:
        f.write(i['name'] + ", " + str(i['saturation']) + "\n")
