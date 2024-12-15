from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


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
