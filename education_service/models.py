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
