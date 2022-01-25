from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/dojo")
def success():
    return "Dojo!"

@app.route("/say/<string:name>")
def hello(name):
    cap_name = name[0].upper() + name[1:]
    return f"Hi {cap_name}!"

@app.route("/repeat/<int:number>/<string:word>")
def repetition(number, word):
    return f"{number * word}"

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def other_routes(path):
    return "Sorry! No response. Try again."

if __name__=="__main__": 
    app.run(debug=True)

