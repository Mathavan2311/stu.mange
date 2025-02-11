import json

FILE="data/stud.json"

def read_json():
    try:
        with open (FILE) as f:
            return json.load(f)
    except:
        with open (FILE,"w") as f:
            temp_dic={"Students":[]}
            json.dump(temp_dic,f,indent=3)
    return temp_dic
    

def write_json(data):
    with open (FILE,"w") as f:
        json.dump(data,f,indent=3)
   


