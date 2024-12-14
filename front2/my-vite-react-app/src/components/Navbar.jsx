import { Link, useLocation } from 'react-router-dom';
import './Navbar.css'

function Navbar() {
    const location = useLocation();

    return (
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <div className="container-fluid">
                <Link className="navbar-brand" to="/">Senior Companion</Link>
                <div className="row"></div>
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarColor02"
                    aria-controls="navbarColor02" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarColor02">
                    <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                        <li className="nav-item">
                            <Link
                                className={`nav-link ${location.pathname === '/' ? 'active' : ''}`}
                                to="/"
                                style={{ color: location.pathname === '/' ? '#333399' : 'black' }}
                            >Home</Link>
                        </li>
                        <li className="nav-item">
                            <Link
                                className={`nav-link ${location.pathname === '/courses' ? 'active' : ''}`}
                                to="/courses"
                                style={{ color: location.pathname === '/courses' ? '#333399' : 'black' }}
                            >Courses</Link>
                        </li>
                        <li className="nav-item">
                            <Link
                                className={`nav-link ${location.pathname === '/assistant' ? 'active' : ''}`}
                                to="/assistant"
                                style={{ color: location.pathname === '/assistant' ? '#333399' : 'black' }}
                            >Assistant</Link>
                        </li>
                    </ul>
                </div>
            </div>

            <div className="col-md-1">
                <img className="fb_img_class" id="facebook" src="/src/assets/fb_img.png" alt="img" />
                <img className="ig_img_class" id="instagram" src="/src/assets/ig_img.png" alt="img" />
            </div>
        </nav>
    );
}

export default Navbar;