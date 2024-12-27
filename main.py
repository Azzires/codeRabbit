from flask import Flask

app = Flask(__name__)

@app.route("/")
def test_project():
    return "Test success"


@app.route("/weather")
def get_weather():
    return "Friday, Sunny, 5 Celsius"