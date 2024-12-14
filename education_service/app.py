from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Klucz potrzebny do sesji i flash

# Przykładowe dane o lekcjach (w prawdziwej aplikacji byłyby pobierane z bazy danych)
lessons = [
    {'id': 1, 'title': 'Wprowadzenie do komputera', 'description': 'Podstawy obsługi komputera.'},
    {'id': 2, 'title': 'Bezpieczeństwo w internecie', 'description': 'Jak dbać o bezpieczeństwo w sieci.'},
    {'id': 3, 'title': 'Zakupy online', 'description': 'Jak robić zakupy przez internet.'},
]

@app.route('/')
def index():
    """Strona główna - lista lekcji"""
    return render_template('index.html', lessons=lessons)

@app.route('/lesson/<int:lesson_id>')
def lesson(lesson_id):
    """Strona pojedynczej lekcji"""
    lesson = next((lesson for lesson in lessons if lesson['id'] == lesson_id), None)
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
        # Możesz dodać logikę do przetwarzania wiadomości (np. zapisywanie do bazy danych, wysyłanie emaili)
        flash('Dziękujemy za wiadomość! Skontaktujemy się z Tobą wkrótce.', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Uruchomienie aplikacji na porcie 5001
