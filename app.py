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


@app.route('/student/add', methods=['POST'])
def new_student():
    global students
    student = request.get_json(force=True)
    student["id"] = data.get_id(students)
    students.append(student)
    return "Added"


@app.route('/student/edit', methods=['POST'])
def update_student():
    global students
    student = request.get_json(force=True)
    students = data.update(students, student)
    return "Updated"


@app.route('/student/delete', methods=['DELETE'])
def delete_student():
    global students
    response = request.get_json(force=True)
    id = response["id"]
    delete_response = data.delete(students, id)
    if delete_response:
        return "Deleted"
    return "id not found, no student deleted!"


if __name__ == "__main__":
    students = data.student_list[:]
    port = int(os.environ.get('PORT', 2700))
    app.run(host='0.0.0.0', port=port)
    # app.run(host='127.0.0.1', port=port)

    
