from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)   # Create a new instance of the Flask class called "app"
@app.route("/")               # The "@" decorator associates this route with the function
# immediately following
def index():
    # Instead of returning a string, we'll return the result of the render_template method, passing
    # in the name of our HTML file
    return render_template("index.html")

# def hello_world():
#     return "Hello World!"     # Return the string "Hello World!" as a response

@app.route("/success")
def success():
    return "Success"

@app.route("/hello/<string:name>/<int:number>")
def hello(name, number):
    # return f"Hello {name * number}"
    return render_template("hello.html", name=name, number=number)

@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
        {'name' : 'Michael', 'age' : 35},
        {'name' : 'John', 'age' : 30 },
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'KB', 'age' : 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], students = student_info)




if __name__=="__main__":  # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    #  Run the app in debug mode
