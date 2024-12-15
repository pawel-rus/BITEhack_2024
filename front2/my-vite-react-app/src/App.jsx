import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import ChatBubble from './components/ChatBubble';
import './styles.css';
import Home1 from './components/Home1';


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
                <Route path="/" element={<Home1 />} />
                <Route path="/courses" element={<Courses />} />
                <Route path="/" element={<Home />} />

            </Routes>
        </Router>
    );
}

export default App;
