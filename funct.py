from utils import *

def regis_stud(name,age,course,address):

    data=read_json()

    temp_data={
        "sino":len(data["Students"])+1,
        "name":name,
        "age":age,
        "course":course,
        "address":address
    }

    data["Students"].append(temp_data)
    try:
        write_json(data) 
        return "success"
    except:
        return "failure"

def delete_stud(id):
    data=read_json()
    for stud in data["Students"]:
          if str(stud["sino"])==id:
               data["Students"].remove(STUD)
               break
    
    sno=1
    for stud in data["Students"]:
         stud["sino"]=sno
         sno+1
    write_json(data)
    

def update_stud(id,name,age,course,address):
    data=read_json()
    for stud in data["Students"]:
          if str(stud["sino"])==id:
               stud["name"]=name,
               stud["age"]=age,
               stud["course"]=course,
               stud["address"]=address,

    write_json(data)