from itertools import count
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "ThisIsSecret'"

@app.route("/")
def index():
    if "count" in session:
        session["count"] += 1
        print("key exists!")
    else:
        session["count"] = 0
        print("key 'count' does NOT exist")
    return render_template("index.html", count=session["count"])

@app.route("/increase", methods=["POST"])
def increase_count():
    # session["count"] += 1
    session["userincrement"] = int(request.form["counter_increment"])
    session["count"] += (session["userincrement"] -1)
    return redirect("/")

@app.route("/destroy_session", methods=["POST"])
def destroy_session():
    # session.clear()
    session.pop("count", None)
    session.pop("userincrement", None)
    return redirect("/")


if __name__=="__main__":
    app.run(debug=True)