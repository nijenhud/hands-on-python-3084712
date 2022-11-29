from distutils.log import debug
from flask import Flask

app = Flask(__name__)


@app.route("/")
def helllo():
    return "Hell, World!"


app.run(debug=True)
