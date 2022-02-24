from flask import Flask

app = Flask(__name__)


@app.route('/')
def counter():
    return 'Hallo From Grunenberg und Comp'
