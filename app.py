from flask import Flask, request, jsonify
from flask_cors import CORS
import json, os, data


app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def hello():
    return "<h2>Welcome to Yinon's Hogwarts CRM Students</h2>"


@app.route('/students', methods=['GET'])
def all_students():
    global students
    return json.dumps(students)


@app.route('/skills', methods=['GET'])
def skills():
    return json.dumps(data.skills_list)


@app.route('/courses', methods=['GET'])
def courses():
    return json.dumps(data.courses_list)


@app.route('/students/add', methods=['POST'])
def new_student():
    global students
    student = request.get_json(force=True)
    student["id"] = data.get_id(students)
    students.append(student)
    return "Added"


@app.route('/students/edit', methods=['POST'])
def update_student():
    global students
    student = request.get_json(force=True)
    students = data.update(students, student)
    return "Updated"


if __name__ == "__main__":
    students = data.student_list[:]
    port = int(os.environ.get('PORT', 2700))
    app.run(host='127.0.0.1', port=port)

    
