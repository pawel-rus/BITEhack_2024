from flask import Flask, render_template, request, redirect, url_for, flash
from models import Lesson  

def init_routes(app):
    @app.route('/')
    def index():
        """Strona główna - lista lekcji"""
        lessons = Lesson.get_all_lessons()  # get all available lessons  from database
        return render_template('index.html', lessons=lessons)

    @app.route('/lesson/<int:lesson_id>')
    def lesson(lesson_id):
        """Strona pojedynczej lekcji"""
        lesson = Lesson.get_lesson_by_id(lesson_id)  
        if lesson:
            return render_template('lesson.html', lesson=lesson)
        else:
            flash('Lekcja nie została znaleziona!', 'error')
            return redirect(url_for('index'))

    @app.route('/contact', methods=['GET', 'POST'])
    def contact():
        """Formularz kontaktowy dla seniorów"""
        if request.method == 'POST':
            name = request.form.get('name')
            email = request.form.get('email')
            message = request.form.get('message')
            flash('Dziękujemy za wiadomość! Skontaktujemy się z Tobą wkrótce.', 'success')
            return redirect(url_for('contact'))
        return render_template('contact.html')
