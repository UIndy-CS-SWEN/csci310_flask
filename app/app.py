from flask import Flask,jsonify,request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
        return "This is a CSCI310 test page!"

@app.route('/json', methods = ['GET'])
def ReturnJSON():
    if(request.method == 'GET'):
        data = {
            "Program" : "Computer Science",
            "Course" : ["Game and GUI Programming",
                        "Operating System",
                        "Algorithem",
                        "Data Structure"]
        }
  
        return jsonify(data)

@app.route('/handle_get', methods=['GET'])
def handle_get():
    if request.method == 'GET':
        name = request.args['name']
        tag = request.args['tag']
        data = {
            "Name" : name,
            "Tag" : tag
        }
  
        return jsonify(data)
    else:
        return "ERROR!"


@app.route('/handle_post', methods=['POST'])
def handle_post():
    if request.method == 'POST':
        name = request.form['name']
        data = {
            "Name" : name,
            "Program" : "Computer Science",
            "Course" : ["Game and GUI Programming",
                        "Operating System",
                        "Algorithem",
                        "Data Structure"]
        }
  
        return jsonify(data)
    else:
        return "POST METHOD ERROR!!"


@app.route('/my_program', methods=['POST'])
def my_program():
    if request.method == 'POST':
        name = request.form['name']
        program = request.form['program']
        cs = {
            "Program" : "Computer Science",
            "Course" : ["Game and GUI Programming",
                        "Operating System",
                        "Algorithem",
                        "Data Structure"]
        }
        me = {
            "Program" : "Mechanical Engineering",
            "Course" : ["CAD",
                        "Static",
                        "Dynamic",
                        "Control System"]
        }
        se = {
            "Program" : "Software Engineering",
            "Course" : ["Introduction to Software Engineering",
                        "Software Testing",
                        "Software Architecture",
                        "Software Project Management"]
        }
        data = {"name": name,
                "programs": ["computer science", 
                             "mechanical engineering",
                             "software engineering"],
                "cs": cs,
                "me": me,
                "se": se
                }
  
        if program == "all":
            return jsonify(data)
        if program == "cs":
            return jsonify(data['cs'])
        if program == "me":
            return jsonify(data['me'])
        if program == "se":
            return jsonify(data['se'])
        return jsonify(data)
    else:
        return "POST METHOD ERROR!!"

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8000)
