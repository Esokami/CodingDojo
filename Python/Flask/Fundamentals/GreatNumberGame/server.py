from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route("/")
def index():
    if "random_int" not in session:
        session["random_int"] = random.randint(1,100)
        print("Random guess created")
    else:
        pass
    return render_template("index.html", random=session["random_int"])

@app.route("/guess", methods=["POST"])
def user_guess():
    session["userguess"] = int(request.form["take_guess"])
    print(f"User input a guess: {session}")
    return redirect("/")

@app.route("/reset", methods=["POST"])
def reset():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)