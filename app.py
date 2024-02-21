from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/cds-services/patient-view', methods=['POST'])
def handle_patient_view_hook():
    # Parse the incoming JSON payload
    data = request.json
    
    # Here, you would insert logic to process the request, such as analyzing patient data
    # For demonstration, we return a static CDS Card as the response

    response = {
        "cards": [
            {
                "summary": "CigStopper (Summary)",
                "indicator": "success",
                "detail": "CigStopper: Based on our analysis, we recommend ..... ",
                "source": {
                    "label": "from CigStopper",
                    "url": "https://www.vanderbilt.edu/"
                },
                "links": [
                    {
                        "label": "Launch CigStopper App",
                        "url": "https://smart.example.com/launch",
                        "type": "smart"
                    }
                ]
            }
        ]
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
