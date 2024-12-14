import { Link, useLocation } from 'react-router-dom';
import './Navbar.css';

function Navbar() {
    const location = useLocation();

    return (
        <nav className="navbar navbar-expand-lg navbar-light">
            <div className="container-fluid">
                {/* Marka */}
                <Link className="navbar-brand" to="/">Senior Companion</Link>

                {/* Przycisk hamburger dla małych ekranów */}
                <button
                    className="navbar-toggler"
                    type="button"
                    data-bs-toggle="collapse"
                    data-bs-target="#navbarColor02"
                    aria-controls="navbarColor02"
                    aria-expanded="false"
                    aria-label="Toggle navigation"
                >
                    <span className="navbar-toggler-icon"></span>
                </button>

                {/* Linki nawigacyjne */}
                <div className="collapse navbar-collapse" id="navbarColor02">
                    <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                        <li className="nav-item">
                            <Link
                                className={`nav-link ${location.pathname === '/' ? 'active' : ''}`}
                                to="/"
                            >
                                Home
                            </Link>
                        </li>
                        <li className="nav-item">
                            <Link
                                className={`nav-link ${location.pathname === '/courses' ? 'active' : ''}`}
                                to="/courses"
                            >
                                Courses
                            </Link>
                        </li>
                        <li className="nav-item">
                            <Link
                                className={`nav-link ${location.pathname === '/assistant' ? 'active' : ''}`}
                                to="/assistant"
                            >
                                Assistant
                            </Link>
                        </li>
                    </ul>
                </div>

                {/* Ikony mediów społecznościowych */}
                <div className="social-icons">
                    <img className="fb_img_class" id="facebook" src="/src/assets/fb_img.png" alt="Facebook" />
                    <img className="ig_img_class" id="instagram" src="/src/assets/ig_img.png" alt="Instagram" />
                </div>
            </div>
        </nav>
    );
}

export default Navbar;
