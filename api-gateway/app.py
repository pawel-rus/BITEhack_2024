from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

MICROSERVICES = {
    "education": "http://localhost:5001",
    "chatbot": "http://localhost:5002",
    "helpdesk": "http://localhost:5003"
}
    
@app.route('/api/<service>/<path:endpoint>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy(service, endpoint):
    if service not in MICROSERVICES:
        return jsonify({"error": "Service not found"}), 404

    # Budowanie żądania do mikroserwisu
    url = f"{MICROSERVICES[service]}/{endpoint}"
    response = requests.request(
        method=request.method,
        url=url,
        headers={key: value for key, value in request.headers if key != 'Host'},
        json=request.get_json(),
        params=request.args
    )
    print("Response status:", response.status_code)
    print("Response content:", response.text)
    return jsonify(response.json()), response.status_code
    
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)
