from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

stores =[
    {
        "name":"My first store",
        "items":
        [
            {
            "name":"first item",
            "price":1.0
            }
        ]
    }
]

@app.route("/")
def home():
    return render_template("index.html")

# POST - used to receive data
# GET - used to send data back only

# POST /store data:{name:}
@app.route("/store", methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store={
        "name":request_data["name"],
        "items":[]
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>
@app.route("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store.get("name",0) == name:
            return jsonify(store)
    return jsonify({"message":"None"})

# GET /store
@app.route("/store")
def get_stores():
    return jsonify({"stores":stores})

# POST /store/<string:name>/item {name:, price:}
@app.route("/store/<string:name>/item", methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store.get("name",0) == name:
            new_item={
                "name":request_data["name"],
                "price":request_data["price"]
            }
            store["items"].append(new_item)
            return jsonify(new_item)
    return jsonify({"message":"None"})

# GET /store/<string:name>/item
@app.route("/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        if store.get("name",0) == name:
            return jsonify({"items":store["items"]})
    return jsonify({"message":"None"})


app.run(port=5000)
