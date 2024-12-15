import jwt
import datetime
from flask import Flask, request, jsonify, render_template
from auth import generate_jwt

def generate_jwt(user_id, secret_key):
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token


def perform_login(username, password):
    user = Users().login(username, password)
    if user == "user":
        return jsonify({'message': 'User not found'}), 404
        
    if user == "password":
        return jsonify({'message': 'Password incorrect'}), 401

    if user:
        try:
            with open('./config.json') as config_file:
                config = json.load(config_file)
            token = jwt.encode({'user_id': user['_id'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)}, 
                                config['secret_key'], algorithm='HS256')
            user["csrftoken"] = token
            #resp = make_response(jsonify({'message': 'login successful', 'user': user}))
            #resp.set_cookie('csrftoken', token, httponly=False, samesite='None', secure=True)
            #return resp
            return jsonify({'message': 'login successful', 'user': user, 'csrf_token': token})
        except Exception as e:
            return jsonify({'message': 'An error occurred', 'error': str(e)}), 500

    return jsonify({
        "message": "Error fetching auth token!, invalid email or password",
        "data": None,
        "error": "Unauthorized"
    }), 404

@auth.route('/auth', methods=['POST'])
def register():
    data = request.get_json()
    
    if 'email' not in data or 'password' not in data or 'username' not in data:
        return jsonify({'error': 'Email, password, and username are flarequired'}), 400
    
    if not re.match(email_regex, data['email']):
        return jsonify({'error': 'Invalid email format'}), 400

    if not re.match(password_regex, data['password']):
        return jsonify({'error': 'Password must contain at least one digit, one uppercase, one lowercase, and one special character'}), 400
    
    existing_user_email = db.user.find_one({"email": data['email']})
    existing_username = db.user.find_one({"username": data['username']})

    if existing_user_email:
        return jsonify({'error': 'Email already exists'}), 400
    
    if existing_username:
        return jsonify({'error': 'Username already exists'}), 400
    
    hashed_password = generate_password_hash(data['password'])

    db.user.insert_one({
        "email": data['email'], 
        "password": hashed_password, 
        "username": data['username'],
        "date_created": datetime.datetime.now()
    })

    return perform_login(data['username'], data['password'])

@auth.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()

        if 'username' not in data or 'password' not in data:
            return jsonify({'message': 'Username and password are required'}), 400

        username = data['username']
        password = data['password']

        return perform_login(username, password)
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500

@auth.route('/logout')
@token_required
def logout(current_user):
    return jsonify({'message': 'logout successful'})