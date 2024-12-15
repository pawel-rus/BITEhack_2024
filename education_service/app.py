from flask import Flask

#from flask_cors import CORS
from config import Config
from models import db
from routes import init_routes
import os

app = Flask(__name__)
app.config.from_object(Config)
#CORS(app)

db.init_app(app)

with app.app_context():
    db.create_all(bind_key='db')  

init_routes(app)

if __name__ == '__main__':
    app.run(port=5001, debug=True) 