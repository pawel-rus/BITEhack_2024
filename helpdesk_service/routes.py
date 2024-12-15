from flask import Flask, request, jsonify
from models import db, HelpDeskPost, Comment

def init_routes(app):

    @app.route('/posts', methods=['POST'])
    def add_post():
        data = request.get_json()
        title = data.get('title')
        description = data.get('description')
        username = data.get('username')
        status="Open"

        if not title or not description or not username:
            return jsonify({"error": "Title, description, and username are required"}), 400

        post = HelpDeskPost(title=title, description=description, status=status, username=username)
        db.session.add(post)
        db.session.commit()
        return jsonify({"message": "Post added successfully"}), 201

    @app.route('/posts', methods=['GET'])
    def get_posts():
        posts = HelpDeskPost.query.order_by(HelpDeskPost.created_at.desc()).all()
        result = []
        for post in posts:
            result.append({
                "id": post.id,
                "title": post.title,
                "description": post.description,
                "created_at": post.created_at,
                "updated_at": post.updated_at,
                "status": post.status,
                "username": post.username,
                "comments": [{"content": comment.content, "username": comment.username, "created_at": comment.created_at} for comment in post.comments]
            })
        print(result)
        return jsonify(result), 200

    @app.route('/comments', methods=['POST'])
    def add_comment():
        data = request.get_json()
        content = data.get('content')
        post_id = data.get('post_id')
        username = data.get('username')

        if not content or not post_id or not username:
            return jsonify({"error": "Content, post_id, and username are required"}), 400

        post = HelpDeskPost.query.get(post_id)
        if not post:
            return jsonify({"error": "Post not found"}), 404

        comment = Comment(content=content, post_id=post.id, user_id=user.id)
        db.session.add(comment)
        db.session.commit()
        return jsonify({"message": "Comment added successfully"}), 201