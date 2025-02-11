from flask import Flask , redirect, render_template, request
from fun import *
app=Flask(__name__)

@app.route("/", methods=["POST","GET"])

def home():
        reg_status= None
        if request.method=="POST":
            reg_status=regis_stud(request.form["name"],request.form["age"],request.form["course"],request.form["address"])
        data=read_json()
        return render_template("index.html",status=reg_status,stud_data=data["Students"])

@app.route("/delete/<id>")

def delete_user(id):
    delete_stud(id)
    return redirect ("/")

@app.route("/update/<id>")

def update_user(id,methods=["GET","POST"]):
    if request.method=="post":
        update_stud(id,request.form["name"],request.form["age"],request.form["course"],request.form["address"])
    return redirect ("/")

     
if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0")