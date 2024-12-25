from flask import Flask

app = Flask(__name__)

@app.route("/")
def test_project():
    return "Test success"