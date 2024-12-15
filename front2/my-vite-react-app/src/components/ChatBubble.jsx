import { useState, useEffect, useRef } from 'react';
import './ChatBubble.css';
import userImage from '../assets/kurson.jpg'; 
import botImage from '../assets/chat_bot.jpg'; 
import microphoneIcon from '../assets/microphone-svgrepo-com.svg'; // Importuj ikonę mikrofonu

function ChatBubble() {
    const [isChatVisible, setChatVisible] = useState(false);
    const [chatHistory, setChatHistory] = useState([
        { prompt: '', response: 'Dzień dobry, w czym mogę ci pomóc?' } // Dodaj domyślną wiadomość
    ]);
    const [prompt, setPrompt] = useState('');
    const [model, setModel] = useState('gemini'); // Dodaj stan dla modelu
    const chatBodyRef = useRef(null);
    const [error, setError] = useState(null);
    const [isListening, setIsListening] = useState(false); // Dodaj stan dla rozpoznawania mowy

    const toggleChat = () => {
        setChatVisible(!isChatVisible);
    };

    const handleModelChange = (selectedModel) => {
        setModel(selectedModel);
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        if (prompt.trim() === "") return;
        try {
            const response = await fetch(`/api/chatbot/ask_${model}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ prompt: prompt }),
            });

            const responseText = await response.text();
            console.log(responseText); // Dodaj ten log, aby zobaczyć odpowiedź serwera

            if (!response.ok) {
                const errorData = JSON.parse(responseText);
                setError(errorData.error || 'An error occurred');
                return;
            }

            const data = JSON.parse(responseText);
            setChatHistory([...chatHistory, { prompt: prompt, response: data.result }]);
            setPrompt('');
            setError(null);

        } catch (err) {
            setError(err.message || 'An error occurred');
        }
    };

    useEffect(() => {
        if (chatBodyRef.current) {
            chatBodyRef.current.scrollTop = chatBodyRef.current.scrollHeight;
        }
    }, [chatHistory]);

    const handleVoiceInput = () => {
        if (!('webkitSpeechRecognition' in window)) {
            alert('Twoja przeglądarka nie obsługuje rozpoznawania mowy.');
            return;
        }

        const recognition = new window.webkitSpeechRecognition();
        recognition.lang = 'pl-PL';
        recognition.interimResults = false;
        recognition.maxAlternatives = 1;

        recognition.onstart = () => {
            setIsListening(true);
        };

        recognition.onresult = (event) => {
            const transcript = event.results[0][0].transcript;
            setPrompt(transcript);
            setIsListening(false);
        };

        recognition.onerror = (event) => {
            console.error('Błąd rozpoznawania mowy:', event.error);
            setIsListening(false);
        };

        recognition.onend = () => {
            setIsListening(false);
        };

        recognition.start();
    };

    return (
        <>
            <button id="chat-toggle-button" onClick={toggleChat}>💬</button>

            <div id="chat-bubble" style={{ visibility: isChatVisible ? 'visible' : 'hidden' }}>
                <div id="chat-bubble-header">Chat with us</div>
                <div id="chat-bubble-body" ref={chatBodyRef}>
                    <div id="chat-history">
                        {chatHistory.map((entry, index) => (
                            <div key={index}>
                                {entry.prompt && (
                                    <div className="user-message">
                                        <img src={userImage} alt="User" />
                                        <p>{entry.prompt}</p>
                                    </div>
                                )}
                                <div className="bot-response">
                                    <img src={botImage} alt="Bot" />
                                    <p>{entry.response}</p>
                                </div>
                            </div>
                        ))}
                        {error && <div className="bot-response"><strong>Error:</strong> {error}</div>}
                    </div>
                </div>
                <div id="chat-bubble-footer">
                    <div id="model-selector">
                        <button
                            className={`model-button ${model === 'gemini' ? 'active' : ''}`}
                            onClick={() => handleModelChange('gemini')}
                        >
                            Gemini
                        </button>
                        <button
                            className={`model-button ${model === 'groq' ? 'active' : ''}`}
                            onClick={() => handleModelChange('groq')}
                        >
                            Groq
                        </button>
                    </div>
                    <form id="chat-form" onSubmit={handleSubmit}>
                        <div className="form-group">
                            <input
                                type="text"
                                className="form-control"
                                id="prompt"
                                name="prompt"
                                required
                                value={prompt}
                                onChange={(e) => setPrompt(e.target.value)}
                                placeholder="Your Question:" // Dodaj placeholder
                            />
                            <button type="button" className="btn btn-secondary" onClick={handleVoiceInput}>
                                <img src={microphoneIcon} alt="Microphone" className="microphone-icon" />
                            </button>
                        </div>
                        <button type="submit" className="btn btn-primary">Ask</button>
                    </form>
                </div>
            </div>
        </>
    );
}

export default ChatBubble;