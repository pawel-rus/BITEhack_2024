from flask import Flask
from flask_cors import CORS
from config import Config
from models import db
from routes import init_routes
import os


app = Flask(__name__, template_folder="../frontend/templates", static_folder='../frontend/static')
app.config.from_object(Config)
CORS(app)

db.init_app(app)

with app.app_context():
    db.create_all(bind_key='db')

init_routes(app)

port = int(os.environ.get('PORT', 5000))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=port, debug=True)
