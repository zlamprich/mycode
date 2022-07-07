#!/usr/bin/python3
  
from flask import Flask
from flask import redirect
from flask import request
from flask import render_template
from flask import url_for
from flask import flash







app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
@app.route("/start")
def start():
    return render_template("challengepage.html")


@app.route("/login", methods = ["POST", "GET"])
def login():
    # POST would likely come from a user interacting with postmaker.html
    if request.method == "POST":
        if request.form.get("nm"): # if nm was assigned via the POST
            return render_template("challengepage2.html")
        else: # if a user sent a post without nm then assign value defaultuser
            flash ("You entered an invalid name!", "info" )
            return redirect(url_for("start"))

@app.route("/questions", methods = ["POST", "GET"])
def questions():
    accepted_answers = {"Zach", "zach", "ZACH"}
    if request.method == "POST":
        if request.form.get("answer"):
            input_answer = request.form.get("answer")
            if input_answer in accepted_answers:
                return redirect(url_for("correct"))
        else:
            flash ("Incorrect answer! Redirecting back to form.", "info")
            return redirect(url_for("questions"))

@app.route("/correct")
def correct():
    return f"Congratulations! You passed the quiz!\n"

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)
