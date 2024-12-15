import { Link } from 'react-router-dom';
import './Home.css';

function Home() {
    return (
        <div className="home">
            <header className="home-header">
                <h1>Witamy w naszym Centrum Edukacyjnym!</h1>
                <p>Odkryj nowy wymiar nauki i wsparcia w naszej platformie.</p>
                <Link to="/courses" className="btn btn-primary">Zobacz kursy</Link>
            </header>

            <section className="instructions">
                <h2>Instrukcja Obsługi</h2>
                <div className="instruction-block">
                    <h3>Chatbot</h3>
                    <p>Nasz Chatbot jest zawsze gotowy do pomocy. Aby go użyć:</p>
                    <ol>
                        <li>Kliknij ikonę 💬 w prawym dolnym rogu, aby otworzyć okno czatu.</li>
                        <li>Wpisz swoje pytanie w polu tekstowym.</li>
                        <li>Możesz też skorzystać z opcji rozpoznawania mowy, klikając ikonę mikrofonu, i dyktować swoje pytanie.</li>
                        <li>Kliknij przycisk "Ask", aby wysłać wiadomość.</li>
                        <li>Chatbot odpowie na Twoje pytanie w okienku.</li>
                        <li>Możesz wybrać model (Gemini lub Groq) za pomocą odpowiedniego przycisku.</li>
                    </ol>
                </div>
                <div className="instruction-block">
                    <h3>Kursy</h3>
                    <p>Nasze kursy pomogą Ci zdobyć nowe umiejętności. Aby z nich skorzystać:</p>
                    <ol>
                        <li>Kliknij przycisk "Zobacz kursy" lub przejdź do zakładki Kursy w menu.</li>
                        <li>Przejrzyj dostępne lekcje i wybierz tę, która Cię interesuje.</li>
                        <li>Kliknij przycisk "Zobacz lekcję", aby wyświetlić tutorial.</li>
                        <li>Postępuj zgodnie z krokami tutorialu, używając przycisku "Następny krok" żeby przechodzić do kolejnych kroków.</li>
                        <li>Możesz zamknąć okienko z tutorialem przyciskiem "Close".</li>
                    </ol>
                </div>
            </section>

            <section className="courses-list">
                <h2>Nasze kursy</h2>
                <ul>
                    <li>Kurs 1: Wprowadzenie do programowania</li>
                    <li>Kurs 2: Zaawansowane techniki programowania</li>
                    <li>Kurs 3: Tworzenie aplikacji webowych</li>
                </ul>
            </section>

            <section className="about-us">
                <h2>O nas</h2>
                <p>Jesteśmy zespołem doświadczonych programistów, którzy chcą dzielić się swoją wiedzą z innymi.</p>
            </section>

            <section className="testimonials">
                <h2>Opinie użytkowników</h2>
                <blockquote>
                    <p>"Świetne kursy! Bardzo mi pomogły w nauce programowania."</p>
                    <footer>- Jan Kowalski</footer>
                </blockquote>
                <blockquote>
                    <p>"Polecam wszystkim, którzy chcą się rozwijać w IT."</p>
                    <footer>- Anna Nowak</footer>
                </blockquote>
            </section>

            <footer className="home-footer">
                <p>&copy; 2024 Nasza Firma. Wszelkie prawa zastrzeżone.</p>
                <Link to="/privacy-policy">Polityka prywatności</Link>
                <Link to="/contact">Kontakt</Link>
            </footer>
        </div>
    );
}

export default Home;