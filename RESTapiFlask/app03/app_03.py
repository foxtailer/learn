from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from sequrity import authenticate, identity
 
app = Flask(__name__)
app.secret_key = "kotik"
api = Api(app)

jwt = JWT(authenticate, identity)  # /auth

items = []

class Item(Resource):
    @jwt_required()
    def get(self,name):
        item = next(filter(lambda x: x["name"] == name, items), None)
        return {"item":item}, 200 if item else 404
    
    def post(self,name):
        if next(filter(lambda x: x["name"] == name, items), None):
            return {"message":f"item {name}, alredy exist"}, 400

        data = request.get_json()
        new_item = {"name":name, "prise":data["price"]}
        items.append(new_item)
        return new_item, 201


class Collection(Resource):
    def get(self):
        return {"items":items}

api.add_resource(Item, "/items/<string:name>")
api.add_resource(Collection, "/items")

app.run(port=5000, debug=True)

   