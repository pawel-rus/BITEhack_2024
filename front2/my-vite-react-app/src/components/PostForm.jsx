import React, { useState } from 'react';

const PostForm = ({ onPostAdded }) => {
    const [nick, setNick] = useState('');
    const [content, setContent] = useState('');
    const [error, setError] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (!nick.trim() || !content.trim()) {
            setError("Nick i treść nie mogą być puste!");
            return;
        }

        try {
            const response = await fetch('/api/helpdesk/posts', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ nick, content }),
            });

            if (response.ok) {
                setNick('');
                setContent('');
                setError('');
                onPostAdded();
            } else {
                const errorData = await response.json();
                setError(errorData.error || errorData.message || 'Wystąpił błąd podczas dodawania postu');
            }
        } catch (error) {
            setError('Wystąpił błąd podczas komunikacji z serwerem');
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            {error && <div className="error-message">{error}</div>}
            <input
                type="text"
                placeholder="Nick"
                value={nick}
                onChange={(e) => setNick(e.target.value)}
            />
            <textarea
                placeholder="Treść posta"
                value={content}
                onChange={(e) => setContent(e.target.value)}
            />
            <button type="submit">Dodaj post</button>
        </form>
    );
};

export default PostForm;