from flask import Flask

app = Flask(__name__)


@app.route('/')
def counter():
<<<<<<< HEAD
    return 'Hallo From Grunenberg und Comp'
=======
    return 'Hello From Grunenberg und Comp!'
>>>>>>> e5d7b1c2a352b8e98ed1f90d7a74be36730e9c9e
