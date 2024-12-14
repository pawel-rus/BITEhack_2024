import sqlite3
import time

import psycopg2
from flask import (current_app, jsonify, redirect, render_template, request, url_for)
from psycopg2 import errors
from models import db


def init_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')