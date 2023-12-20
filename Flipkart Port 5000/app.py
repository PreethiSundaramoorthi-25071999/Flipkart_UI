from flask import Flask,render_template,request,url_for,redirect,session
import sqlite3 as sql

app=Flask(__name__)
app.secret_key="key"

@app.route('/')
def login():
    conn=sql.connect("product_details.db")
    conn.row_factory=sql.Row
    cur=conn.cursor()
    cur.execute("select * from login_table")
    data=cur.fetchall()
    return render_template("home.html",data=data)

@app.route("/form",methods=["POST","GET"])
def form():
    if request.method=="POST":
        Name=request.form.get("Name")
        Password=request.form.get("Password")
        conn=sql.connect("product_details.db")
        conn.row_factory=sql.Row
        cur=conn.cursor()
        cur.execute("select * from login_table")
        data=cur.fetchone()
        if data:
            if str(data["Name"])==Name and str(data["Password"])==Password:
                return redirect(url_for("login"))     
    return render_template("form.html")

@app.route("/add",methods=["GET","POST"])
def add_user():
    if request.method=="POST":
     Name=request.form.get("Name")
     Password=request.form.get("Password")
     conn=sql.connect("product_details.db")
     cur=conn.cursor()
     cur.execute("Insert into login_table(NAME,PASSWORD) values(?,?)",
         (Name,Password)) 
     conn.commit() 
     return redirect(url_for("login"))
    return render_template("add_user.html")

@app.route("/logout")
def logout():
    session.pop("Name",None)
    return redirect(url_for("form"))

@app.route('/page1',methods=["POST","GET"])
def home():
    if request.method=="POST":
        var1=request.json
        conn=sql.connect("product_details.db")
        conn.row_factory=sql.Row
        cur=conn.cursor()
        cur.execute("Insert into product_table(PRODUCT_NAME,RATING,QUANTITY,IMAGE,PRICE) values(?,?,?,?,?)",
         (var1['Product_Name'],var1['Rating'],var1['Quantity'],var1['Image'],var1['Price'])) 
        conn.commit() 
        return redirect(url_for('login'))
    conn=sql.connect("product_details.db")
    conn.row_factory=sql.Row
    cur=conn.cursor()
    cur.execute("select * from product_table")
    data=cur.fetchall()
    return render_template("product.html",datum=data)
    
if __name__=="__main__":
    app.run(debug=True,port=5000)
