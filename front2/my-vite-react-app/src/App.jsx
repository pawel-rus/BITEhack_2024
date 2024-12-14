import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import ChatBubble from './components/ChatBubble';
import './styles.css';
function Home() {
    return <div>Home page</div>
}
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