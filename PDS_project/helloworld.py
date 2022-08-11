from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/")
@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def registerUtil(username, password):
    if not register(username, password):
        return "Invalid Data format. Please make sure your username "\
                "and password meets security requirements"


if __name__ == "__main__":
    app.run(debug=True)
