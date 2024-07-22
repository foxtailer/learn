from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
 
app = Flask(__name__)
api = Api(app)

items = [{"name":"test", "prise":"test"}]

#jwt = JWTManager(app, authenticate, identity)  # /auth
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)


class User:
    def __init__(self, _id, username, password) -> None:
        self.id = _id
        self.username = username
        self.password = password

users = [User(1, "Bob", "abcd")]


username_mapping = {u.username:u for u in users}
userid_mapping = {u.id:u for u in users}

@app.route("/login", methods=["POST"])
def authenticate():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = username_mapping.get(username, None)

    if user and user.password == password:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    else:  
        return jsonify({"msg": "Bad username or password"}), 401

class Item(Resource):
    @jwt_required()
    def get(self,name):
        item = next(filter(lambda x: x["name"] == name, items), None)
        return {"item":item}, 200 if item else 404
    
    def post(self,name):
        if next(filter(lambda x: x["name"] == name, items), None):
            return {"message":f"item {name}, alredy exist"}, 400

        data = request.get_json() # if request from browser dont have a proper header or json attach this line give an error
        new_item = {"name":name, "prise":data["prise"]}
        items.append(new_item)
        return new_item, 201
    
    def delete(self, name):
        global items
        items = list(filter(lambda x:x["name"] != name, items))
        return {"message":"Item was deleated!"}
    
    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "prise",
            type=float,
            required = True,
            help = "This field cannot be left bland!"
        )
        #data = request.get_json()
        data = parser.parse_args()
         
        item = next(filter(lambda x:x["name"] == name, items), None)
        if item is None:
            item = {"name":name, "prise":data["prise"]}
            items.append(item)
        else:
            item.update(data)
        return item


class Collection(Resource):
    def get(self):
        return {"items":items}

api.add_resource(Item, "/items/<string:name>")
api.add_resource(Collection, "/items")

app.run(port=5000, debug=True)
