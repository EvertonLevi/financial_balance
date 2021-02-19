from datetime import datetime
from random import randrange

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from sqlalchemy import create_engine

db_connect = create_engine('sqlite:///db.db')
app = Flask(__name__)
CORS(app)
api = Api(app)

class User(Resource):

    def post(self):
        conn = db_connect.connect()
        id = randrange(0, 1001, 2)
        name = request.json['name']
        email = request.json['email']
        senha = request.json['senha']
        conn.execute("insert into user values('{0}', '{1}', '{2}', '{3}')".format(
            id, name, email, senha))
        query = conn.execute("select * from user order by id desc limit 1")
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)


class Launchs(Resource):

    @app.route('/', methods=['GET'])
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from launch")
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

    def post(self):
        conn = db_connect.connect()
        launch = request.json['launch']
        description = request.json['description']
        idUser = request.json['idUser']
        date = datetime.now()
        conn.execute("insert into launch values(null, '{0}', '{1}', '{2}', '{3}')".format(
            launch, description, date, idUser))
        query = conn.execute("select * from launch order by id desc limit 1")
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        print(datetime.now())
        return jsonify(result)

    def put(self):
        conn = db_connect.connect()
        id = request.json['id']
        launch = request.json['launch']
        description = request.json['description']
        date = datetime.now()
        conn.execute("update launch set launch ='" + str(launch) +
                     "', description ='" + str(description)
                     +
                     "', date ='" + str(date) + "'  where id =%d " % int(id))
        query = conn.execute("select * from launch where id=%d " % int(id))
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)


class LaunchById(Resource):

    def get(self, id):
        conn = db_connect.connect()
        query = conn.execute("select * from launch where id=%d" % int(id))
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

    def delete(self, id):
        conn = db_connect.connect()
        conn.execute("delete from launch where id=%d" % int(id))
        return {"status": "success"}


api.add_resource(User, '/user')
api.add_resource(Launchs, '/launchs')
api.add_resource(LaunchById, '/launchs/<id>')

if __name__ == '__main__':
    app.run(host="0.0.0.0")
