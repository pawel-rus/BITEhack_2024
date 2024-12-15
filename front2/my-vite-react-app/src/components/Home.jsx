import { Link } from 'react-router-dom';
import './Home.css';

function Home() {
    return (
        <div className="home">
            <header className="home-header">
                <h1>Witamy w Centrum Edukacyjnym!</h1>
                <p>Prosta nauka dla każdego, w każdym wieku.</p>
            </header>

            <section className="instructions">
                <h2><span role="img" aria-label="instructions">📖</span> Jak korzystać?</h2>
                <div className="instruction-block">
                    <h3><span role="img" aria-label="chatbot">🤖</span> Chatbot</h3>
                    <p>Nasz chatbot jest tutaj, by Ci pomóc:</p>
                    <div>
                        <li>Kliknij ikonę 💬 w prawym dolnym rogu.</li>
                        <li>Wpisz swoje pytanie i naciśnij "Wyślij".</li>
                        <li>Możesz również użyć mikrofonu, by mówić do chatbota.</li>
                    </div>
                </div>
                <div className="instruction-block">
                    <h3><span role="img" aria-label="courses">📚</span> Kursy</h3>
                    <p>Ucz się z naszych kursów krok po kroku:</p>
                    <div>
                        <li>Przejdź do sekcji "Kursy".</li>
                        <li>Wybierz kurs i rozpocznij naukę.</li>
                    </div>
                </div>
            </section>
            
            <section className="about-us">
                <h2><span role="img" aria-label="about us">👨‍🏫</span> O nas</h2>
                <p>Jesteśmy zespołem, który pasjonuje się edukacją i nowymi technologiami.</p>
            </section>

            <footer className="home-footer">
                <p>&copy; 2024 Nasza Firma. Wszelkie prawa zastrzeżone.</p>
                <Link to="/privacy-policy">Polityka prywatności</Link> | 
                <Link to="/contact">Kontakt</Link>
            </footer>
        </div>
    );
}

export default Home;
