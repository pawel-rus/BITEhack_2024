import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import ChatBubble from './components/ChatBubble';
import Courses from './components/Courses';

import Home from './components/Home';
import './styles.css';
import Home1 from './components/Home1';


function Assistant() {
    return <div>Assistant page</div>
}

function App() {
    return (
        <Router>
            <Navbar />
            <ChatBubble />
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/courses" element={<Courses />} />
                <Route path="/assistant" element={<Home1 />} />
            </Routes>
        </Router>
    );
}

export default App;