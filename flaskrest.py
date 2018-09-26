from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)

users = {1: {'name': 'Warren'},
         2: {'name': 'Addison'},
         3: {'name': 'Parker'}
         }

thingstodo = {
         1: ['wakeup', 'code', 'shower'],
         2: ['dance', 'eat', 'read'],
         3: ['play', 'watch', 'eat']
        }

@app.route('/user', methods=['GET'])
def getcurrentuser():
    msg = {'msg': 'returning current user',
            'user': {
                'username': 'Warren Wrate',
                'favorite color': 'green'
            }}
    return jsonify(msg)

@app.route('/user/<int:userid>', methods=['GET'])
def getuser(userid):
    user = users.get(userid, None)
    return jsonify(user)

#works with http://localhost:5000/things/?userid=2
@app.route('/things/', methods=['GET'])
def getthings():
    u_id = request.args.get('userid')
    if u_id:
        print("found id:",u_id)
    else:
        print('userid is not coming through')
    things = thingstodo.get(int(u_id), None )
    return jsonify(things)

@app.route('/things', methods=['POST'])
def getaddthings():
    data = request.get_json()
    print('thing param', data, type(data))
    userid = data['userid']
    thing = data['thing']
    thingstodo[userid].append(thing)
    things = thingstodo.get(int(userid), None )
    return jsonify(things)

if __name__ == '__main__':
    app.run(debug=True, port=5000)