import os
from urllib.parse import quote_plus

#postgresql://postgres:GWnQGFuMpUnZxayhsYrtEdGoOnXUxCpd@junction.proxy.rlwy.net:37394/railway

password = quote_plus(os.getenv('DB_PASSWORD', 'API_KEY'))
db_host = os.getenv('DB_HOST', 'junction.proxy.rlwy.net')
db_port = os.getenv('DB_PORT', '37394')
db_name = os.getenv('DB_NAME', 'railway')
db_user = os.getenv('DB_USER', 'postgres')

DATABASE_URL = f"postgresql://{db_user}:{password}@{db_host}:{db_port}/{db_name}"

class Config:
    SQLALCHEMY_BINDS = {
        'db': DATABASE_URL
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False

