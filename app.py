from flask import flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello"



if__name__=="__main__":
    app.run(debug=True)