from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from auth import generate_jwt, token_required
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


# MODELE
class Thread(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.String(50), nullable=False)
    comments = db.relationship('Comment', backref='thread', lazy=True)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    thread_id = db.Column(db.Integer, db.ForeignKey('thread.id'), nullable=False)
    user_id = db.Column(db.String(50), nullable=False)
    text = db.Column(db.Text, nullable=False)


# ENDPOINTY
@app.route('/')
def index():
    return render_template('help_desk.html')


@app.route('/threads', methods=['GET', 'POST'])
@token_required
def threads(current_user):
    if request.method == 'POST':
        title = request.json.get('title')
        if not title:
            return jsonify({'error': 'Missing thread title'}), 400

        thread = Thread(title=title, user_id=current_user)
        db.session.add(thread)
        db.session.commit()
        return jsonify({'message': 'Thread created successfully'}), 201

    threads = Thread.query.all()
    return jsonify([{'id': t.id, 'title': t.title, 'user_id': t.user_id} for t in threads])


@app.route('/threads/<int:thread_id>/comments', methods=['GET', 'POST'])
@token_required
def comments(current_user, thread_id):
    thread = Thread.query.get(thread_id)
    if not thread:
        return jsonify({'error': 'Thread not found'}), 404

    if request.method == 'POST':
        text = request.json.get('text')
        if not text:
            return jsonify({'error': 'Missing comment text'}), 400

        comment = Comment(thread_id=thread_id, user_id=current_user, text=text)
        db.session.add(comment)
        db.session.commit()
        return jsonify({'message': 'Comment added successfully'}), 201

    comments = Comment.query.filter_by(thread_id=thread_id).all()
    return jsonify([{'id': c.id, 'text': c.text, 'user_id': c.user_id} for c in comments])


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=5001)
