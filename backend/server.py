from datetime import datetime
from random import randrange

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import (JWTManager, create_access_token,
                                get_jwt_identity, jwt_required)
from flask_restful import Api, Resource
from sqlalchemy import create_engine

db_connect = create_engine('sqlite:///db.db')
app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)
CORS(app)
api = Api(app)


class User(Resource):

    @app.route("/login", methods=["POST"])
    def login():
        conn = db_connect.connect()
        id = randrange(0, 1001, 2)
        name = request.json['name']
        senha = request.json['senha']
        email = request.json['email']
        access_token = create_access_token(identity=name)
        # conn.execute("insert into user values('{0}', '{1}', '{2}', '{3}')".format(
        #     id, name, senha, email))
        # query = conn.execute("select * from user order by id desc limit 1")
        # result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        # return jsonify(result)
        return jsonify(access_token=access_token)

    @app.route("/protegido", methods=["GET"])
    @jwt_required()
    def protected():
        current_user = get_jwt_identity()
        return jsonify(logged_in_as=current_user), 200

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
