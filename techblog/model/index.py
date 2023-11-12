from flask import Flask, json, request, jsonify

import base
from students import Student

app = Flask(__name__)

@app.route('/students/<id>')
def list_students(id):
    session = base.Session()
    student = session.query(Student).filter(Student.umich_id == id).first()
    print(f"| {student.umich_id} | {student.first_name} {student.last_name} | {student.major} |")
    return student.as_dict()