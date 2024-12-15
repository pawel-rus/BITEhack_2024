from flask import Flask, request, jsonify, send_from_directory
import requests
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

MICROSERVICES = {
    "education": "http://localhost:5001",
    "chatbot": "http://127.0.0.1:5002",
    "helpdesk": "http://localhost:5003"
}
    
@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'help_desk.html')

@app.route('/api/<service>/<path:endpoint>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy(service, endpoint):
    if service not in MICROSERVICES:
        return jsonify({"error": "Service not found"}), 404

    # Budowanie żądania do mikroserwisu
    url = f"{MICROSERVICES[service]}/{endpoint}"
    print("Forwarding request to:", url)
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
    
# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:GWnQGFuMpUnZxayhsYrtEdGoOnXUxCpd@junction.proxy.rlwy.net:37394/railway'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)


@app.route('/get_entries', methods=['GET'])
def get_entries():
    with app.app_context():
        db.create_all()
        entries = Entry.query.order_by(Entry.id).all()
        return jsonify([{
            'id': entry.id,
            'username': entry.username,
            'content': entry.content
        } for entry in entries])

# with app.app_context():
#     db.create_all()
#     entries = Entry.query.order_by(Entry.id).all()
#     print([{
#         'id': entry.id,
#         'username': entry.username,
#         'content': entry.content
#     } for entry in entries])

if __name__ == '__main__':
    app.run(debug=True, port=5000)
