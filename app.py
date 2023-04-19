from flask import Flask

app = Flask(__name__)

@app.get('/welcome')
def welcome():
    """Returns welcome at /welcome endpoint"""

    return 'welcome'


@app.get('/welcome/home')
def welcome_home():
    """Returns welcome at /welcome/home endpoint"""

    return 'welcome home'


@app.get('/welcome/back')
def welcome_back():
    """Returns welcome at /welcome/back endpoint"""

    return 'welcome back'


