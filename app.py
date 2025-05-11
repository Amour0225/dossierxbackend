import os

# Vérification du fichier
csv_path = "dossierx_match_data.csv"

if os.path.exists(csv_path):
    print("Fichier trouvé, chargement en cours...")
else:
    raise FileNotFoundError(f"Erreur : Le fichier '{csv_path}' est introuvable.")
from flask import Flask, jsonify
import pandas as pd
import os

app = Flask(__name__)

@app.route('/api/match-predictions')
def match_predictions():
    file_path = os.path.join(os.getcwd(), 'dossierx_match_data.csv')
    if not os.path.exists(file_path):
        return jsonify({"error": "Fichier dossierx_match_data.csv introuvable"}), 404

    df = pd.read_csv(file_path)
    return df.to_json(orient='records'), 200

if __name__ == '__main__':
    app.run(debug=True)
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
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Dossier X Backend API is running'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Récupération des données envoyées depuis le frontend
    var_input = data.get('var_input')
    corners_input = data.get('corners_input')

    # Logique temporaire (remplace plus tard par ton vrai modèle)
    var_prediction = 'VAR probable' if var_input else 'VAR improbable'
    corners_prediction = 'Plus de 10 corners' if corners_input else 'Moins de 10 corners'

    return jsonify({
        'var_prediction': var_prediction,
        'corners_prediction': corners_prediction
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
