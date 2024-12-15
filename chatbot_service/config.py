import os
from urllib.parse import quote_plus
from dotenv import load_dotenv

load_dotenv()
password = quote_plus(os.getenv('DB_PASSWORD'))
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
# print(password, db_host, db_port, db_name, db_user)

DATABASE_URL = f"postgresql://{db_user}:{password}@{db_host}:{db_port}/{db_name}"

class Config:
    SQLALCHEMY_BINDS = {
        'db': DATABASE_URL  
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False
