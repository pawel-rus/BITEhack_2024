import  { useState, useEffect, useRef } from 'react';
import './ChatBubble.css';

function ChatBubble() {
    const [isChatVisible, setChatVisible] = useState(false);
    const [chatHistory, setChatHistory] = useState([]);
    const [prompt, setPrompt] = useState('');
    const chatBodyRef = useRef(null);
    const [error, setError] = useState(null);

    const toggleChat = () => {
        setChatVisible(!isChatVisible);
    };


    const handleSubmit = async (event) => {
        event.preventDefault();
        if (prompt.trim() === "") return;
        try {
            const response = await fetch('/ask_ai', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ prompt: prompt }),
            });

            if (!response.ok) {
                const errorData = await response.json();
                setError(errorData.error || 'An error occurred');
                return
            }

            const data = await response.json();
            setChatHistory([...chatHistory, { prompt: prompt, response: data.result }]);
            setPrompt('');
            setError(null)

        } catch (err) {
            setError(err.message || 'An error occurred')
        }
    };


    useEffect(() => {
        if (chatBodyRef.current) {
            chatBodyRef.current.scrollTop = chatBodyRef.current.scrollHeight;
        }
    }, [chatHistory]);


    return (
        <>
            <button id="chat-toggle-button" onClick={toggleChat}>💬</button>

            <div id="chat-bubble" style={{ visibility: isChatVisible ? 'visible' : 'hidden' }}>
                <div id="chat-bubble-header">Chat with us</div>
                <div id="chat-bubble-body" ref={chatBodyRef}>
                    <div id="chat-history">
                        {chatHistory.map((entry, index) => (
                            <div key={index}>
                                <p><strong>You:</strong> {entry.prompt}</p>
                                <p><strong>Bot:</strong> {entry.response}</p>
                            </div>
                        ))}
                        {error && <p><strong>Error:</strong> {error}</p>}
                    </div>
                </div>
                <form id="chat-form" onSubmit={handleSubmit}>
                    <div className="form-group">
                        <label htmlFor="prompt">Your Question:</label>
                        <input
                            type="text"
                            className="form-control"
                            id="prompt"
                            name="prompt"
                            required
                            value={prompt}
                            onChange={(e) => setPrompt(e.target.value)}
                        />
                    </div>
                    <button type="submit" className="btn btn-primary">Ask</button>
                </form>
            </div>
        </>
    );
}

export default ChatBubble;