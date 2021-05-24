from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Welcome to Code Plateau; The second silicon Valley</p>"

@app.route("/home")
def home():
    return "<b>Welcome</b>"

@app.route("/about us")
def aboutus():
    return "<b>We are destined to making available all kinds of softwares for programmers to fork and also programming a better life to all mankind</b>"

@app.route("/contact us")
def contactus():
    return "<b>we are located at no.5 slicon valley street</b>"

@app.route("/products")
def products():
    return "<b>softwares of various kinds</b>"

@app.route("/services")
def services():
    return "<b>our services are both home and away</b>"