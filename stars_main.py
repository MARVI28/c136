from flask import Flask,jsonify,request
from stars import data

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "data":data
    })
@app.route("/stars")
def stars():
    name = request.args.get("name")
    stars_data = next(i for i in data if i ["name"] == name)
    return jsonify({
        "stars_data":stars_data
    })
app.run()