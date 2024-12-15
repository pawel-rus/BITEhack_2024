import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import ChatBubble from './components/ChatBubble';
import Home from './components/Home'; 
import Courses from './components/Courses';
import HelpDesk from './components/HelpDesk';

import './styles.css';

function App() {
    return (
        <Router>
            <Navbar />
            <ChatBubble />
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/courses" element={<Courses />} />
                <Route path="/helpdesk" element={<HelpDesk />} />
            </Routes>
        </Router>
    );
}

export default App;