import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import ChatBubble from './components/ChatBubble';
import Home from './components/Home'; 
import Courses from './components/Courses';
import HelpDesk from './components/HelpDesk';

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
                <Route path="/helpdesk" element={<HelpDesk />} />
            </Routes>
        </Router>
    );
}

export default App;