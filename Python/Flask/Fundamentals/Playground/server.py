from flask import Flask, render_template
app = Flask(__name__)

@app.route("/play")
def index():
    return render_template("index.html", number = 3, color = "powderblue")

@app.route("/play/<int:number>")
def multiply(number):
    return render_template("index.html", number = number, color ="powderblue")

@app.route("/play/<int:number>/<string:color>")
def color(number, color):
    return render_template("index.html", number = number, color = color)

if __name__=="__main__":
    app.run(debug = True)