from flask import Flask

app = Flask(__name__)

@app.route("/")
def test_project():
    """
    Test if the project is working correctly.
    
    Returns:
        str: 'Test success' message indicating successful test execution
    """
    return "Test success"