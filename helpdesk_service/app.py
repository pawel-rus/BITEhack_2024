from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from auth import generate_jwt, token_required
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('help_desk.html')

@app.route('/login', methods=['POST'])
def login():
    user_id = request.json.get('user_id')
    password = request.json.get('password')
    
    if not user_id or not password:
        return jsonify({'error': 'Missing user_id or password'}), 400
    
    # Weryfikacja poświadczeń
    if user_id in users_db and users_db[user_id] == password:
        token = generate_jwt(user_id, app.config['SECRET_KEY'])
        return jsonify({'token': token})
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/report', methods=['POST'])
#@token_required
def report_problem(current_user):
    description = request.json.get('description')
    if not description:
        return jsonify({'error': 'Missing description'}), 400
    
    problem = Problem(description=description, user_id=current_user)
    db.session.add(problem)
    db.session.commit()
    return jsonify({'message': 'Problem reported successfully'})

@app.route('/problems', methods=['GET'])
@token_required
def get_problems(current_user):
    problems = Problem.query.all()
    return jsonify([{'id': p.id, 'description': p.description, 'status': p.status, 'user_id': p.user_id} for p in problems])

@app.route('/problems/<int:problem_id>/resolve', methods=['POST'])
@token_required
def resolve_problem(current_user, problem_id):
    problem = Problem.query.get(problem_id)
    if not problem:
        return jsonify({'error': 'Problem not found'}), 404
    
    problem.status = 'resolved'
    db.session.commit()
    return jsonify({'message': 'Problem resolved successfully'})

if __name__ == '__main__':
    app.run(debug=True, port=5001)