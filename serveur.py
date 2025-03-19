from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'Aucun fichier trouvé'}), 400

    file = request.files['file']
    df = pd.read_excel(file)

    data = df.to_dict(orient='records')  # Convertir les données en liste de dictionnaires
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
