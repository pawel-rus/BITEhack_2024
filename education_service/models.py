from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Lesson(db.Model):
    __bind_key__ = 'db'  

    __tablename__ = 'lessons' 

    id = db.Column(db.Integer, primary_key=True)  
    title = db.Column(db.String(120), nullable=False) 
    description = db.Column(db.Text, nullable=False)  

    def __repr__(self):
        return f'<Lesson {self.title}>'

    @classmethod
    def get_all_lessons(cls):
        """Metoda do pobierania wszystkich lekcji z bazy"""
        return cls.query.all()  

    @classmethod
    def get_lesson_by_id(cls, lesson_id):
        """Metoda do pobierania lekcji na podstawie ID"""
        return cls.query.get(lesson_id)  




class Tutorial(db.Model):
    __bind_key__ = 'db'
    __tablename__ = 'tutorials'

    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lessons.id'), nullable=False, unique=True)  # Unikalny klucz obcy
    steps = db.Column(db.JSON, nullable=False)  # JSON przechowujący kroki tutorialu

    def __repr__(self):
        return f'<Tutorial for Lesson {self.lesson_id}>'

    @classmethod
    def get_tutorial_by_lesson_id(cls, lesson_id):
        """Metoda do pobierania tutorialu na podstawie ID lekcji"""
        return cls.query.filter_by(lesson_id=lesson_id).first()

    @classmethod
    def get_tutorial_by_id(cls, tutorial_id):
        """Metoda do pobierania tutorialu na podstawie jego ID"""
        return cls.query.get(tutorial_id)

















# class Quiz(db.Model):
#     __bind_key__ = 'db'
#     __tablename__ = 'quizzes'

#     id = db.Column(db.Integer, primary_key=True)
#     question = db.Column(db.String(255), nullable=False)
#     options = db.Column(db.JSON, nullable=False)  # Przechowujemy opcje jako JSON
#     correct_answer = db.Column(db.String(255), nullable=False)  # Poprawna odpowiedź
#     lesson_id = db.Column(db.Integer, db.ForeignKey('lessons.id'), nullable=False)

#     def __repr__(self):
#         return f'<Quiz {self.question}>'

#     @classmethod
#     def get_quizzes_by_lesson_id(cls, lesson_id):
#         """Metoda do pobierania wszystkich quizów dla lekcji na podstawie ID"""
#         return cls.query.filter_by(lesson_id=lesson_id).all()