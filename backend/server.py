from datetime import datetime
from random import randrange

from flask import Flask, Response, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import (JWTManager, create_access_token,
                                create_refresh_token, get_jwt_identity,
                                jwt_required, set_access_cookies,
                                set_refresh_cookies)
from flask_restful import Api, Resource
from flask_restful import reqparse

from sqlalchemy import create_engine

db_connect = create_engine('sqlite:///db.db')
app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)
CORS(app)
api = Api(app)


class User(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("name",
                        type=str,
                        required=True,
                        help="This fild cannot be blank.")
    parser.add_argument("senha",
                        type=str,
                        required=True,
                        help="This fild cannot be blank")

    @app.route("/loginTest", methods=["POST"])
    def loginTest():
        email = request.json.get("email", None)
        senha = request.json.get("senha", None)
        if email == "" or senha == "":
            return jsonify({"msg": "Bad username or password"}), 401

        access_token = create_access_token(identity=senha)
        return jsonify(access_token=access_token)

    @app.route("/login", methods=["POST"])
    def login():
        conn = db_connect.connect()
        senha = request.json['senha']
        email = request.json['email']
        user = jsonify({'senha': senha, 'email': email})
        if not user:
            access_token = create_access_token(identity=user.senha, fresh=True)
            refresh_token = create_refresh_token(user.senha)
            return {
                'access_token': access_token,
                'refresh_token': refresh_token
            }, 200

        return jsonify({"Message: "}, {"Invalid Credentials"}), 401

    @app.route("/protegido", methods=["GET"])
    @jwt_required()
    def protected():
        current_user = get_jwt_identity()
        return jsonify(logged_in_as=current_user), 200

    @app.route("/register", methods=["POST"])
    def post():
        conn = db_connect.connect()
        id = randrange(0, 1001, 2)
        name = request.json['name']
        email = request.json['email']
        senha = request.json['senha']
        access_token = create_access_token(identity=senha)
        conn.execute("insert into user values('{0}', '{1}', '{2}', '{3}')".format(
            id, name, email, access_token))
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


api.add_resource(Launchs, '/launchs')
api.add_resource(LaunchById, '/launchs/<id>')


# if __name__ == '__main__':
#     app.run(host="0.0.0.0")
