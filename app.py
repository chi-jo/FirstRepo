from flask import Flask

app = Flask(__name__)


@app.route('/')
def counter():
    return 'Hallo von Grunenberg und Comp!!'
