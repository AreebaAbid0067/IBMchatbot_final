from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# IBM Watson API details
IBM_WATSON_URL = "https://us-south.ml.cloud.ibm.com/ml/v1/deployments/00a7d919-6547-4b9d-86f0-0fd0bd476886/text/generation?version=2023-05-29"
IBM_WATSON_ACCESS_TOKEN = "eyJraWQiOiIyMDI0MDgwMzA4NDEiLCJhbGciOiJSUzI1NiJ9.eyJpYW1faWQiOiJJQk1pZC02OTIwMDBJUEUwIiwiaWQiOiJJQk1pZC02OTIwMDBJUEUwIiwicmVhbG1pZCI6IklCTWlkIiwianRpIjoiYmJlOGQwMjctNTk0NC00ODhjLTgxYWYtMDEyNGQ2N2NhZDU1IiwiaWRlbnRpZmllciI6IjY5MjAwMElQRTAiLCJnaXZlbl9uYW1lIjoiQXJlZWJhIiwiZmFtaWx5X25hbWUiOiJBYmlkIiwibmFtZSI6IkFyZWViYSBBYmlkIiwiZW1haWwiOiJhYXJlZWJhMDA2QGdtYWlsLmNvbSIsInN1YiI6ImFhcmVlYmEwMDZAZ21haWwuY29tIiwiYXV0aG4iOnsic3ViIjoiYWFyZWViYTAwNkBnbWFpbC5jb20iLCJpYW1faWQiOiJJQk1pZC02OTIwMDBJUEUwIiwibmFtZSI6IkFyZWViYSBBYmlkIiwiZ2l2ZW5fbmFtZSI6IkFyZWViYSIsImZhbWlseV9uYW1lIjoiQWJpZCIsImVtYWlsIjoiYWFyZWViYTAwNkBnbWFpbC5jb20ifSwiYWNjb3VudCI6eyJ2YWxpZCI6dHJ1ZSwiYnNzIjoiYTVkMDllMDA4NjZmNDA3NDhkNzM4NzYyZDQzOGI5OTIiLCJpbXNfdXNlcl9pZCI6IjEyNjI2MjExIiwiZnJvemVuIjp0cnVlLCJpbXMiOiIyNzQ0OTQ2In0sImlhdCI6MTcyNDU4MDQ0NSwiZXhwIjoxNzI0NTg0MDQ1LCJpc3MiOiJodHRwczovL2lhbS5jbG91ZC5pYm0uY29tL2lkZW50aXR5IiwiZ3JhbnRfdHlwZSI6InVybjppYm06cGFyYW1zOm9hdXRoOmdyYW50LXR5cGU6YXBpa2V5Iiwic2NvcGUiOiJpYm0gb3BlbmlkIiwiY2xpZW50X2lkIjoiZGVmYXVsdCIsImFjciI6MSwiYW1yIjpbInB3ZCJdfQ.dlR1D6STwD2mq5yBD8TfyQ4Ijyo5iNeWvDFCG24fEfSwZvy2y9IwyP9wnfmUHluQ_vHPjfb08Ew5tf2gLog7lGG8MB7CwUM15692tY0YjPn2ADXx1nm5KvN-aZEa7060QbhX5BdMQntXy53HYC5HikI66TZWUbvfMy45FGWSy6aMTTt_-huZ3t131dJ4Gh1JDEOeQj3sUWqB0CLghSmk-eaU_I-Ec5nawnXMQ1fI5iNqBVHgNIq8vF_ma3aniAbz4BAoD-loonPrSUnKTwhxGeRyhvonSE-TP0fU66zPwYAAXoYicWS3PZRaQUEDVvtG8fSDL16NE86k534otrqjbw"  # Replace with your actual access token

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

        # Make a POST request to the IBM Watson API
        response = requests.post(IBM_WATSON_URL, json=payload, headers=headers)
        
        if response.status_code == 200:
            response_data = response.json()
            generated_text = response_data.get("generated_text", "No response from the model.")
            return jsonify({"generated_text": generated_text})
        else:
            return jsonify({"error": "Failed to generate text", "details": response.text}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
