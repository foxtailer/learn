from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

response_data = ""
@app.route("/", methods=['POST'])
def create_store():
  global response_data
  response_data += (request.form["user_data"] + "& #13;" + "& #10;") 
  return render_template("index.html", response_data=response_data)

app.run(port=5000)