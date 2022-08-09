from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Hello, World!</h1>"

@app.route("/login")
def login():
    return "<h1>Login Page</h1>"

if __name__ == "__main__":
    app.run(debug=True)