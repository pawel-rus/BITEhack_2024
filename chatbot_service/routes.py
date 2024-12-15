import sqlite3
import time
import psycopg2
from flask import (current_app, jsonify, redirect, render_template, request, url_for)
from psycopg2 import errors
from models import db
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings
from llama_index.llms.groq import Groq
from llama_index.core import StorageContext
from llama_index.core import load_index_from_storage
import os

api_key = os.getenv('LLM_API_KEY')

llm = Groq(model="llama-3.1-8b-instant", api_key=api_key)

def init_routes(app):  
    @app.route('/ask_ai', methods=['POST'])
    def query_endpoint():
        try:
            index_dir = './final_index'
        
            Settings.embed_model = HuggingFaceEmbedding(
                model_name="BAAI/bge-small-en-v1.5"
            )
            
            data = request.get_json()
            print(data.get('prompt'))
            prompt = data.get('prompt')
            storage_context = StorageContext.from_defaults(persist_dir=index_dir)
            index = load_index_from_storage(storage_context)
            
            chat_engine = index.as_chat_engine(chat_mode="condense_question", llm=llm, verbose=True)

            response_node = chat_engine.chat(prompt)  # chat here
            print({'result':  response_node.response})
            return jsonify({'result':  response_node.response})
        except Exception as e:
            return jsonify({'error':  f"An error occurred: {e}"})
        
    @app.route('/courses')
    def courses():
        return render_template('courses.html')
        
    @app.route('/assistant')
    def assistant():
        return render_template('assistant.html')
        
        