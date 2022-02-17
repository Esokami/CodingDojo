#Tweet creation

from crypt import methods


@app.route("/tweet/create", methods=["POST"])
def createTweet():
    # Validations here...
    data = {
        "content" : request.form["content"],
        "location" : request.form["location"],
        # Pass in the id of the User in session to se as the foreign key to describe who made the tweet
        "user_id" : session["user_id"]
    }
    Tweet.save(data)
    # ...