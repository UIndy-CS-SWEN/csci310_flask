from flask import Flask,jsonify,request
app = Flask(__name__)

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


if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8000)
