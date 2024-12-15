from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__)

# Konfiguracja bazy danych
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:GWnQGFuMpUnZxayhsYrtEdGoOnXUxCpd@junction.proxy.rlwy.net:37394/railway'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)

# Model bazy danych
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nick = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

# Inicjalizacja bazy danych
with app.app_context():
    db.create_all()

# Endpoint do tworzenia postów
@app.route('/api/helpdesk/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    nick = data.get('nick')
    content = data.get('content')
    if not nick or not content:
        return jsonify({'error': 'Nick i treść są wymagane'}), 400
    date = datetime.now()

    new_post = Post(nick=nick, content=content, date=date)
    db.session.add(new_post)
    db.session.commit()
    return jsonify({'message': 'Post dodany pomyślnie'}), 201

# Endpoint do pobierania postów
@app.route('/api/helpdesk/posts', methods=['GET'])
def get_posts():
    posts = Post.query.order_by(Post.date.desc()).all()
    post_list = []
    for post in posts:
        post_list.append({
            'id': post.id,
            'nick': post.nick,
            'content': post.content,
            'date': post.date.strftime('%Y-%m-%d %H:%M:%S')
        })
    return jsonify(post_list), 200

if __name__ == '__main__':
    app.run(debug=True, port=5003)  # Uruchamiamy na porcie 5003