# routes.py
from flask import Blueprint, render_template, request, redirect, url_for, flash

routes = Blueprint('routes', __name__)

# Sample lesson data
lessons = [
    {'id': 1, 'title': 'Wprowadzenie do komputera', 'description': 'Podstawy obsługi komputera.'},
    {'id': 2, 'title': 'Bezpieczeństwo w internecie', 'description': 'Jak dbać o bezpieczeństwo w sieci.'},
    {'id': 3, 'title': 'Zakupy online', 'description': 'Jak robić zakupy przez internet.'},
]

@routes.route('/')
def index():
    """Strona główna - lista lekcji"""
    return render_template('index.html', lessons=lessons)

@routes.route('/lesson/<int:lesson_id>')
def lesson(lesson_id):
    """Strona pojedynczej lekcji"""
    lesson = next((lesson for lesson in lessons if lesson['id'] == lesson_id), None)
    if lesson:
        return render_template('lesson.html', lesson=lesson)
    else:
        flash('Lekcja nie została znaleziona!', 'error')
        return redirect(url_for('routes.index'))

@routes.route('/contact', methods=['GET', 'POST'])
def contact():
    """Formularz kontaktowy dla seniorów"""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # Procesowanie wiadomości
        flash('Dziękujemy za wiadomość! Skontaktujemy się z Tobą wkrótce.', 'success')
        return redirect(url_for('routes.contact'))
    return render_template('contact.html')