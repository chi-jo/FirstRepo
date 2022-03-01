from flask import Flask

app = Flask(__name__)


@app.route('/')
def counter():
    return 'Guten Morgen von Grunenberg und Comp!'
