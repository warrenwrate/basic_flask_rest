from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

users = {
    1: {'usrname': 'warren'},
    2: {'username': 'addison'},
    3: {'username': 'parker'},
    4: {'username': 'jessica'}
}

class Hello(Resource):
    def get(self):
        return jsonify({'msg':'Hello world!'})

class Multi(Resource):
    def get(self, num):
        return jsonify({'msg':num})

class User(Resource):
    def get(self, userid):
        print('entered id', userid)
        user = users[userid]
        return jsonify(user)

    def post(self):
        newid = len(users) + 1
        data = request.get_json()
        userdata = data['user']
        users[newid] = userdata
        msg = {'msg': 'user saved successfully'}
        return jsonify(msg)

api.add_resource(Hello, '/')
api.add_resource(User, '/user', '/user/<int:userid>')
api.add_resource(Multi, '/multi/<int:num>')

if __name__ == '__main__':
    app.run(debug=True, port=3000)

        
