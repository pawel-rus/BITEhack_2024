from flask import Flask, render_template, jsonify, request, redirect, url_for, flash
from models import Lesson  

def init_routes(app):
    @app.route('/lessons', methods=['GET', 'POST'])
    def index():
        """Strona główna - lista lekcji"""
        lessons = Lesson.get_all_lessons() 
         # get all available lessons  from database
        lessons_data = [{"id": lesson.id, "title": lesson.title, "description": lesson.description} for lesson in lessons]

        return jsonify(lessons_data), 200
        #return render_template('index.html', lessons=lessons)

    @app.route('/lesson/<int:lesson_id>')
    def lesson(lesson_id):
        """Strona pojedynczej lekcji"""
        lesson = Lesson.get_lesson_by_id(lesson_id)  
        if lesson:
            lesson_data = {
                "id": lesson.id,
                "title": lesson.title,
                "description": lesson.description
            }
            return jsonify(lesson_data), 200  # Zwracamy dane w formacie JSON
        else:
            return jsonify({"error": "Lekcja nie została znaleziona!"}), 404

    @app.route('/contact', methods=['POST'])
    def contact():
        """Odbiera dane z formularza kontaktowego i potwierdza w JSON"""
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        if not name or not email or not message:
            return jsonify({"error": "Wszystkie pola są wymagane!"}), 400  # Zwracamy błąd 400, jeśli dane są niekompletne
        
        # Tutaj możesz przetworzyć lub zapisać dane kontaktowe
        return jsonify({"message": "Dziękujemy za wiadomość! Skontaktujemy się z Tobą wkrótce."}), 200
