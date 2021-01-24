from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from datetime import datetime
from json import dumps

db_connect = create_engine('sqlite:///db.db')
app = Flask(__name__)
api = Api(app)


class Launchs(Resource):

    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from launch")
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

    def post(self):
        conn = db_connect.connect()
        launch = request.json['launch']
        description = request.json['description']
        date = datetime.now()
        conn.execute("insert into launch values(null, '{0}', '{1}', '{2}')".format(
            launch, description, date))
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

if __name__ == '__main__':
    app.run()
