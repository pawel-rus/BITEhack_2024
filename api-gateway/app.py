from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Adresy mikroserwisów (dla przykładu)
#MICROSERVICE_CHAT_BOT_URL = "http://localhost:5001"
MICROSERVICE_EDUCATION_URL = "http://127.0.0.1:5001"

@app.route('/lesson/<int:lesson_id>', methods=['GET'])
def lesson(lesson_id):
    """Endpoint rejestracji użytkownika"""

    # Przekazanie zapytania do mikroserwisu A (obsługuje użytkowników)
    response = requests.post(f"{MICROSERVICE_EDUCATION_URL}/lesson/{lesson_id}")
    
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({"error": "Sperma"}), response.status_code
    


@app.route('/lessons')
def index():
    """Strona główna - lista lekcji"""
    response = requests.post(f"{MICROSERVICE_EDUCATION_URL}/lessons")

    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({"error": "Sperma"}), response.status_code
    
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)
