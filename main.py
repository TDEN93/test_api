from flask import Flask
from flask_restful import Resource, Api, reqparse
from datetime import date

STUDENTS = {
    '1': {'name': 'player1', 'age': 28, 'mood': 'good'},
    '2': {'name': 'player2', 'age': 24, 'mood': 'good'},
}


app = Flask(__name__)
api = Api(app)


parser = reqparse.RequestParser()

class StudentsList(Resource):
    def get(self):
        return STUDENTS



api.add_resource(StudentsList, '/players/')


if __name__ == "__main__":
    app.run(debug=True)