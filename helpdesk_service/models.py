from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class HelpDeskPost(db.Model):
    __bind_key__ = 'db'
    __tablename__ = 'help_desk_post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, onupdate=datetime.utcnow)
    status = db.Column(db.String(50), default='Open', nullable=False)
    username = db.Column(db.String(50), nullable=False)

class Comment(db.Model):
    __bind_key__ = 'db'
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('help_desk_post.id'), nullable=False)
    post = db.relationship('HelpDeskPost', backref=db.backref('comments', lazy=True))
