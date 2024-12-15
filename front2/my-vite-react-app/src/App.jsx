import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import ChatBubble from './components/ChatBubble';
import Home from './components/Home';
import './styles.css';


function Courses() {
    return <div>Courses page</div>
}
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
                <Route path="/assistant" element={<Assistant />} />
            </Routes>
        </Router>
    );
}

export default App;