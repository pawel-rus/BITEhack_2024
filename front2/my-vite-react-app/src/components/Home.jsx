import { Link } from 'react-router-dom';
import './Home.css';

function Home() {
    return (
        <div className="home">
            <header className="home-header">
                <h1>Witamy na naszej stronie!</h1>
                <p>Oferujemy szeroki wybór kursów online, które pomogą Ci zdobyć nowe umiejętności.</p>
                <Link to="/courses" className="btn btn-primary">Zobacz kursy</Link>
            </header>
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