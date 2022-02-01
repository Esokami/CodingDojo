from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "ThisIsSecret"
# our index route will handle rendering our form
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/users", methods=["POST"])
def create_user():
    print("Got Post Info")
    session["username"] = request.form["name"]  # Here we add 2 properties to session to store the name and email
    session["useremail"] = request.form["email"]
    # Never render a template on a POST request.
    # Instead we will redirect to our index route.
    return redirect("/show")

#adding this method
@app.route("/show")
def show_user():
    # return render_template("show.html", name_on_template=session["username"],
    # email_on_template=session["useremail"])
    return render_template("show.html")

if __name__=="__main__":
    app.run(debug=True)