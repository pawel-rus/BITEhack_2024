from flask import Flask, request, jsonify, render_template
from auth import generate_jwt

app = Flask(__name__)
secret_key = 'your_secret_key'

# Przykładowa baza danych użytkowników
users_db = {
    'user1': 'password1',
    'user2': 'password2'
}

@app.route('/')
def index():
    return render_template('auth.html')

