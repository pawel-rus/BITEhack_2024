from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins during development

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:GWnQGFuMpUnZxayhsYrtEdGoOnXUxCpd@junction.proxy.rlwy.net:37394/railway'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)

# Removed create_all as we are now relying on migrations
with app.app_context():
   db.create_all()

@app.route('/add_entry', methods=['POST'])
def add_entry():
    data = request.get_json()
    username = data.get('username')
    content = data.get('content')

    print(data)

    if not username or not content:
        return jsonify({'error': 'Username and content are required'}), 400

    entry = Entry(username=username, content=content)
    db.session.add(entry)
    db.session.commit()

    return jsonify({'message': 'Entry added successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)