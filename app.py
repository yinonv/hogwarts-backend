from flask import Flask, request, jsonify
import json, os
from flask_cors import CORS
from data import student_list as students
from data import skills_list
from data import courses_list


app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def hello():
    return "Hello from hogwarts!"


@app.route('/students', methods=['GET'])
def all_students():
    global students
    return json.dumps(students)


@app.route('/skills', methods=['GET'])
def skills():
    return json.dumps(skills_list)


@app.route('/courses', methods=['GET'])
def courses():
    return json.dumps(courses_list)


@app.route('/students/add/', methods=['POST'])
def new_student():
    global students
    student = request.get_json(force=True)
    students.append(student)
    return "Added"


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

    