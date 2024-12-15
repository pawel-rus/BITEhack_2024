from flask import Flask, render_template, jsonify, request, redirect, url_for, flash
from models import Lesson, Tutorial

def init_routes(app):
    @app.route('/lessons', methods=['GET'])
    def index():
        """Strona główna - lista lekcji"""
        lessons = Lesson.get_all_lessons() 
         # get all available lessons  from database
        lessons_data = [{"id": lesson.id, "title": lesson.title, "description": lesson.description} for lesson in lessons]

        return jsonify(lessons_data), 200
        #return render_template('index.html', lessons=lessons)

    @app.route('/lesson/', methods=['GET'])
    def lesson():
        """Strona pojedynczej lekcji"""
        data = request.get_json()
        lesson_id = data.get('lesson_id')

        if not lesson_id:
            return jsonify({"error": "lesson_id is required!"}), 400

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

    @app.route('/tutorial/', methods=['GET'])
    def tutorial():
        """Strona z tutorialem danej lekcji"""
        data = request.get_json()
        lesson_id = data.get('lesson_id')

        if not lesson_id:
            return jsonify({"error": "lesson_id is required!"}), 400

        tutorial = Tutorial.get_tutorial_by_lesson_id(lesson_id)

        if tutorial:
            return jsonify(tutorial.steps), 200  
        else:
            return jsonify({"error": "Tutorial nie został znaleziony dla tej lekcji!"}), 404