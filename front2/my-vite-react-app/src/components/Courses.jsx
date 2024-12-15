import React, { useState, useEffect } from 'react';
import './Courses.css';
//import 'bootstrap/dist/css/bootstrap.min.css'; // Import Bootstrap CSS

function Courses() {
    const [courses, setCourses] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [tutorial, setTutorial] = useState(null);
    const [selectedLessonId, setSelectedLessonId] = useState(null);
    const [showModal, setShowModal] = useState(false);
    const [currentStep, setCurrentStep] = useState(1);

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

    const fetchTutorial = async (lessonId) => {
        try {
            const response = await fetch('api/education/tutorial/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ lesson_id: lessonId }),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
             // Zresetuj currentStep za każdym razem przy pobieraniu nowego tutorialu
           setCurrentStep(1);
            setTutorial(data);
            setShowModal(true);
        } catch (err) {
            setError(err.message);
        }
    };

  const handleViewLesson = (lessonId) => {
        setSelectedLessonId(lessonId);
        setTutorial(null);
        fetchTutorial(lessonId);
  };

   const closeModal = () => {
        setShowModal(false);
        setTutorial(null);
        setSelectedLessonId(null);
        setCurrentStep(1); // Zresetuj currentStep przy zamknięciu modala
    };

    const handleNextStep = () => {
      if (tutorial && currentStep < Object.keys(tutorial).length) {
            setCurrentStep(prevStep => prevStep + 1);
      }
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
         <div className="container mt-5 p-4 border rounded shadow-sm bg-white">
            <h2 className="mb-4 text-primary">Wybierz lekcję:</h2>
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
           <div className={`modal fade ${showModal ? 'show d-block' : ''}`} id="tutorialModal" tabIndex="-1" role="dialog" style={{ display: showModal ? 'block' : 'none' }}>
               <div className="modal-dialog modal-dialog-centered">
                   <div className="modal-content">
                       <div className="modal-header">
                         <h5 className="modal-title">Tutorial for Lesson: {selectedLessonId}</h5>
                         <button type="button" className="btn-close" data-bs-dismiss="modal" onClick={closeModal} aria-label="Close"></button>
                       </div>
                     <div className="modal-body">
                           {tutorial && tutorial[currentStep] && (
                            <div style={{ marginBottom: '15px', fontSize: '1.2rem' }}>
                                <div style={{ fontWeight: 'bold', color: '#007bff' }}>
                                    Krok {currentStep}:
                                </div>
                                <div style={{ fontSize: '1.1rem' }}>{tutorial[currentStep]}</div>
                            </div>
                        )}
                         {tutorial && !tutorial[currentStep] && (
                            <p style={{ fontStyle: 'italic', color: '#888' }}>Tutorial zakończony.</p>
                        )}
                        </div>
                        <div className="modal-footer">
                                  {tutorial && currentStep < Object.keys(tutorial).length ? (
                               <button type="button" className="btn btn-primary" onClick={handleNextStep}>
                                   Następny krok
                                </button>
                                   ) : null}
                           <button type="button" className="btn btn-secondary" onClick={closeModal} data-bs-dismiss="modal">Close</button>
                        </div>
                    </div>
                </div>
            </div>
              {showModal && <div className="modal-backdrop fade show"></div>}
        </div>
    );
}

export default Courses;