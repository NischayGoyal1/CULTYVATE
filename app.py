from flask import Flask, redirect,render_template, request,redirect,session
from weath import *

app=Flask(__name__)

@app.route("/")
def start():
    return render_template("index.html")

@app.route("/sen",methods=["POST"])
def fetch():
    name=request.form["Name"]
    phn=request.form["Ph-Number"]
    phn="+91"+phn
    mal=request.form["E-mail"]
    lo=request.form["loc"]
    dic=nisch(lo)
    return redirect("/")
    

app.run(debug=False)
