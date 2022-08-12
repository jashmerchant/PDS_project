from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("home.html")

<<<<<<< HEAD:PDS_project/helloworld.py
@app.route("/")
@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def registerUtil(username, password):
    if not register(username, password):
        return "Invalid Data format. Please make sure your username "\
                "and password meets security requirements"

=======
@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    return render_template("register.html")
>>>>>>> c2d48693217ac126f36574480adc1afcc93d6e04:PDS_project/app.py

if __name__ == "__main__":
    app.run(debug=True)
