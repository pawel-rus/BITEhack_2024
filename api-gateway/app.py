from flask import Flask, request, jsonify
import requests
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

MICROSERVICES = {
    "education": "http://localhost:5001",
    "chatbot": "http://127.0.0.1:5002",
    "helpdesk": "http://localhost:5003"
    }  

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
    try:
        response_json = response.json()
    except ValueError:
        return response.text, response.status_code

    return jsonify(response_json), response.status_code
    
# # Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:GWnQGFuMpUnZxayhsYrtEdGoOnXUxCpd@junction.proxy.rlwy.net:37394/railway'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_BINDS'] = {
    'db': 'postgresql://postgres:GWnQGFuMpUnZxayhsYrtEdGoOnXUxCpd@junction.proxy.rlwy.net:37394/railway'
}

db = SQLAlchemy(app)

class HelpDeskPost(db.Model):
    __tablename__ = 'help_desk_post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, onupdate=datetime.utcnow)
    status = db.Column(db.String(50), default='Open', nullable=False)
    username = db.Column(db.String(50), nullable=False)

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('help_desk_post.id'), nullable=False)
    post = db.relationship('HelpDeskPost', backref=db.backref('comments', lazy=True))

# Ensure tables are created before defining relationships
with app.app_context():
    db.create_all()

@app.route('/get_entries', methods=['GET'])
def get_entries():
    with app.app_context():
        db.create_all()
        entries = HelpDeskPost.query.order_by(HelpDeskPost.id).all()
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
