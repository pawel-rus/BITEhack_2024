import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    SERVICE_URLS = {
        'auth_service': os.getenv('AUTH_SERVICE_URL', 'http://localhost:5001'),
        'helpdesk_service': os.getenv('HELPDESK_SERVICE_URL', 'http://localhost:5002')
    }