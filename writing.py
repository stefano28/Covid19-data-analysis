import json 
  
def write_json(data, filename='slope.json'): 
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4) 
      
def update(date, slope_ic, slope_h):
    with open('slope.json') as json_file: 
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
            "slope_h": slope_h
        } 
    
        temp.append(y) 
        
    write_json(data)

def restore():
    with open('slope.json','w') as f:
        tmp = []
        json.dump(tmp,f)

