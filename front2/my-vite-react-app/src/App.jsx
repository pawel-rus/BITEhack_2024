import { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import ChatBubble from './components/ChatBubble';
import './styles.css';
import { loadEntries, addEntry } from './components/helpers/helpers'; //Import the functions

function Home() {
    return <div>Home page</div>
}
function Courses() {
    return <div>Courses page</div>
}
function Assistant() {
    const [entries, setEntries] = useState([]);
    const [username, setUsername] = useState('');
    const [content, setContent] = useState('');

    useEffect(() => {
        loadEntries(setEntries);
    }, []);

    const handleAddEntry = async () => {
        await addEntry(username, content, () => loadEntries(setEntries), setUsername, setContent);
    };

    return (
        <div>
            <div>
                <h1>Blog Entries</h1>
                <div id="entries">
                    {entries.map((entry, index) => (
                        <div key={index} className="entry">
                            <div className="username">{entry.username}</div>
                            <div className="timestamp">{entry.timestamp}</div>
                            <div>{entry.content}</div>
                        </div>
                    ))}
                </div>

                <h2>Add New Entry</h2>
                <div>
                    <input
                        type="text"
                        id="username"
                        placeholder="Username"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                    />
                    <textarea
                        id="content"
                        placeholder="Content"
                        value={content}
                        onChange={(e) => setContent(e.target.value)}
                    />
                    <button onClick={handleAddEntry}>Add Entry</button>
                </div>
            </div>
        </div>
    );
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