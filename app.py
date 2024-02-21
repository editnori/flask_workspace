from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/model-endpoint', methods=['GET'])
def model_endpoint():
    # Placeholder for future model processing
    return jsonify({"message": "If you see this message the deployment trigger worked"})

if __name__ == '__main__':
    app.run(debug=True)