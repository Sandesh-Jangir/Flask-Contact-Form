from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("Home.html", options=['Query','Feedback','Complaint','Other'])
@app.route("/result", methods=['GET', 'POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    comment_type = request.form['comment-type']
    comment = request.form['comment']
    return render_template("Result.html", data = [name,email,comment_type,comment])


if __name__ == "__main__":
    app.run(debug=True)