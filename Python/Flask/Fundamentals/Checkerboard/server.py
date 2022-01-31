from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<int:number>")
def changeHeight(number):
    return render_template("index.html", number = number)

if __name__=="__main__":
    app.run(debug=True)