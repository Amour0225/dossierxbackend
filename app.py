from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/predict/var", methods=["POST"])
def predict_var():
    return jsonify({"VAR_expected": True})

@app.route("/predict/corners", methods=["POST"])
def predict_corners():
    return jsonify({"more_corners_expected": False})

@app.route("/")
def index():
    return "Dossier X Backend API is running."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
