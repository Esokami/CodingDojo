from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    session["username"] = request.form["user_name"]
    session["userlocation"] = request.form["dojo_location"]
    session["userlanguage"] = request.form["fav_language"]
    session["usercomment"] = request.form["comment"]
    return redirect("/result")

@app.route("/result")
def show_result():
    return render_template("results.html")

if __name__=="__main__":
    app.run(debug=True)