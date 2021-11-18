from flask import Flask
from flask_restful import Resource, Api, reqparse
from datetime import date

STUDENTS = {
    '1': {'name': 'Tray', 'age': 28, 'mood': 'good', 'playtime_start': "today", 'meditation': True, 'meditation_length': 5, 'hours_slept': 8, 'breakfast': False, 'lunch': True, 'dinner': False,
  'caffeine_amount_in_mg': 400, 'water_amount_in_oz': 16},
    '2': {'name': 'Vincent', 'age': 0, 'mood': 'good', 'playtime_start': "today", 'meditation': True, 'meditation_length': 6, 'hours_slept': 8, 'breakfast': False, 'lunch': True, 'dinner': False,
  'caffeine_amount_in_mg': 400, 'water_amount_in_oz': 16},
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