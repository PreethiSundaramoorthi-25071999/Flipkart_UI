from flask import Flask,render_template,request
import requests
import sqlite3 as sql
import json

app=Flask(__name__)

@app.route('/',methods=["POST","GET"])
def home2():
    if request.method=="POST":
        Product_Name=request.form.get("Product_Name")
        Rating=request.form.get("Rating")
        Quantity=request.form.get("Quantity")
        Image=request.form.get("Image")
        Price=request.form.get("Price")
        dict1={}
        dict1.update({"Product_Name":Product_Name})
        dict1.update({"Rating":Rating})
        dict1.update({"Quantity":Quantity})
        dict1.update({"Image":Image})
        dict1.update({"Price":Price})
        url="http://127.0.0.1:5000/page1"
        response=requests.post(url,json=dict1)
        return{"data":"response"}
    return render_template("userform.html")

if __name__=="__main__":
    app.run(debug=True,port=5001)