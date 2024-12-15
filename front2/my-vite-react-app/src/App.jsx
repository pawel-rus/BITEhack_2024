import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import ChatBubble from './components/ChatBubble';
<<<<<<< HEAD
=======
import Courses from './components/Courses';

import Home from './components/Home';
>>>>>>> 1ceadcfec3fd3e160ed1a99b0b28a506de8acc2b
import './styles.css';
import Home1 from './components/Home1';


<<<<<<< HEAD
function Home() {
    return <div>Home page</div>
}

function Courses() {
    return <div>Courses page</div>
}

=======
>>>>>>> 1ceadcfec3fd3e160ed1a99b0b28a506de8acc2b
function Assistant() {
    return <div>Assistant page</div>
}

function App() {
    return (
        <Router>
            <Navbar />
            <ChatBubble />
            <Routes>
                <Route path="/" element={<Home1 />} />
                <Route path="/courses" element={<Courses />} />
<<<<<<< HEAD
                <Route path="/" element={<Home />} />

=======
                <Route path="/assistant" element={<Home1 />} />
>>>>>>> 1ceadcfec3fd3e160ed1a99b0b28a506de8acc2b
            </Routes>
        </Router>
    );
}

export default App;
