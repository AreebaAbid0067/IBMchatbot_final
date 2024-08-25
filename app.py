from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(_name_)
CORS(app)  # Allow CORS for all domains

# IBM Watson API details (this is a mock setup for the demo)
IBM_WATSON_URL = "https://us-south.ml.cloud.ibm.com/ml/v1/deployments/00a7d919-6547-4b9d-86f0-0fd0bd476886/text/generation?version=2023-05-29"
IBM_WATSON_ACCESS_TOKEN = ""  # Replace with your actual access token

# Root route for the server
@app.route('/', methods=['GET'])
def index():
    return "Welcome to the Chatbot Backend API"

# Main endpoint for generating text
@app.route('/generate-text', methods=['POST'])
def generate_text():
    try:
        data = request.json
        text_input = data.get("input", "")
        parameters = data.get("parameters", {})

        # Prepare the payload for the IBM Watson API
        payload = {
            "input": text_input,
            "parameters": parameters
        }

        headers = {
            "Authorization": f"Bearer {IBM_WATSON_ACCESS_TOKEN}",
            "Content-Type": "application/json"
        }

        # For the sake of this demo, we're not actually calling the IBM API
        # Instead, we'll return a mock response
        generated_text = f"Mocked response for: {text_input}"
        return jsonify({"generated_text": generated_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if _name_ == '_main_':
    app.run(debug=True)