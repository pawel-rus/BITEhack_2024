import React, { useState, useEffect } from 'react';
import './Courses.css';

function Courses() {
    const [courses, setCourses] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [tutorial, setTutorial] = useState(null); // Stan do przechowywania danych tutorialu
    const [selectedLessonId, setSelectedLessonId] = useState(null); // ID wybranej lekcji

    const fetchCourses = async () => {
        setLoading(true);
        setError(null);

        try {
            const response = await fetch('api/education/lessons', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: 'give me data' }),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            setCourses(data);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    // Funkcja do pobierania tutorialu (używając POST)
    const fetchTutorial = async (lessonId) => {
        try {
            const response = await fetch('api/education/tutorial/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ lesson_id: lessonId }), // Wysyłamy lesson_id jako JSON
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            setTutorial(data);  // Przypisujemy dane tutorialu do stanu
        } catch (err) {
            setError(err.message);
        }
    };

    // Funkcja do obsługi kliknięcia w przycisk "Zobacz lekcję"
    const handleViewLesson = (lessonId) => {
        setSelectedLessonId(lessonId);  // Ustawiamy ID lekcji
        setTutorial(null);               // Resetujemy stan tutorialu przy zmianie lekcji
        fetchTutorial(lessonId);         // Pobieramy tutorial dla tej lekcji
    };

    useEffect(() => {
        fetchCourses();
    }, []);

    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>Error: {error}</div>;
    }

    return (
        <div>
            {/* Wyświetlamy listę kursów */}
            <section>
                <h2 className="mb-4">Wybierz lekcję:</h2>
                <div className="row">
                    {courses.map(course => (
                        <div key={course.id} className="col-md-4 mb-3">
                            <div className="card">
                                <div className="card-body">
                                    <h5 className="card-title">{course.title}</h5>
                                    <p className="card-text">{course.description}</p>
                                    <button
                                        onClick={() => handleViewLesson(course.id)}
                                        className="btn btn-primary"
                                    >
                                        Zobacz lekcję
                                    </button>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
            </section>

            {/* Wyświetlamy tutorial dla wybranej lekcji */}
            {selectedLessonId && tutorial && (
    <section>
        <h2 style={{ fontSize: '2rem', fontWeight: 'bold', marginBottom: '20px' }}>
            Tutorial dla lekcji: {selectedLessonId}
        </h2>
        <div style={{ padding: '20px', backgroundColor: '#f4f4f4', borderRadius: '8px' }}>
            {tutorial ? (
                <div>
                    {Object.entries(tutorial).map(([stepNumber, step], index) => (
                        <div key={index} style={{ marginBottom: '15px', fontSize: '1.2rem' }}>
                            <div style={{ fontWeight: 'bold', color: '#007bff' }}>
                                Krok {stepNumber}:
                            </div>
                            <div style={{ fontSize: '1.1rem' }}>{step}</div>
                        </div>
                    ))}
                </div>
            ) : (
                <p style={{ fontStyle: 'italic', color: '#888' }}>Brak kroków w tym tutorialu.</p>
            )}
        </div>
    </section>
)}


        </div>
    );
}

export default Courses;
