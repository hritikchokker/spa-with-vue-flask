from flask import Flask, jsonify, request
from flask_cors import CORS
from courses import COURSES
import uuid
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/', methods=['GET'])
def helloWorld():
    response_object = {'status': 'success'}
    response_object['message'] = 'Hello World From Flask'
    return response_object


@app.route('/courses', methods=['GET', 'POST'])
def all_courses():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        COURSES.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'paperback': post_data.get('paperback'),
            'price': post_data.get('price')
        })
        response_object['message'] = 'Course added!'
    else:
        response_object['courses'] = COURSES
    return jsonify(response_object)


@app.route('/courses/<course_id>', methods=['GET', 'PUT', 'DELETE'])
def single_course(course_id):
    response_object = {'status': 'success'}
    if request.method == 'GET':
        return_course = ''
        for course in COURSES:
            if course['id'] == course_id:
                return_course = course
        response_object['course'] = return_course
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_course(course_id)
        COURSES.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'paperback': post_data.get('paperback'),
            'price': post_data.get('price')
        })
        response_object['message'] = 'Course updated!'
    if request.method == 'DELETE':
        remove_course(course_id)
        response_object['message'] = 'Course removed!'
    return jsonify(response_object)


def remove_course(course_id):
    for course in COURSES:
        if course['id'] == course_id:
            COURSES.remove(course)
            return True
    return False


if __name__ == '__main__':
    app.run()
