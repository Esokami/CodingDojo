from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<int:number>")
def changeHeight(number):
    return render_template("index.html", number = number)

@app.route("/<int:number>/<int:num2>")
def changeBoth(number, num2):
    return render_template("index.html", number = number, num2 = num2)

@app.route("/<int:number>/<int:num2>/<string:color_1>/<string:color_2>")
def alternateColors(number, num2, color_1, color_2):
    return render_template("index.html", number = number, num2 = num2, color_1 = color_1, color_2 = color_2)

if __name__=="__main__":
    app.run(debug=True)