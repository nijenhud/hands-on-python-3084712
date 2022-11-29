import csv
from flask import Flask, render_template, request, jsonify
from pprint import pprint


app = Flask(__name__)

with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)


@app.route("/")
def index():
    # template found in templates/index.html
    return render_template("index.html")


@app.route("/laureates/")
def laureate_list():
    # template found in templates/laureate.html
    results = []

    # Your code here!
    search_string = request.args.get("surname").lower().strip()
    results = list(
        filter(lambda l: (search_string in l["surname"].lower()), laureates))
    # results.append(tmp_list)
    return jsonify(results)


app.run(debug=True)
