import  { useState, useEffect } from 'react';
import './HelpDesk.css';

const HelpDesk = () => {
    const [posts, setPosts] = useState([]);
    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');
    const [username, setUsername] = useState('');
    const [commentContent, setCommentContent] = useState('');
    const [selectedPostId, setSelectedPostId] = useState(null);

    const fetchPosts = async () => {
        const response = await fetch('/api/helpdesk/posts');
        const data = await response.json();
        setPosts(data);
    };

    useEffect(() => {
        fetchPosts();
    }, []);

    const handleAddPost = async () => {
        const response = await fetch('/api/helpdesk/posts', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ title, description, username }),
        });
        if (response.ok) {
            fetchPosts();
            setTitle('');
            setDescription('');
            setUsername('');
        }
    };

    const handleAddComment = async (postId) => {
        const response = await fetch('/api/helpdesk/comments', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ content: commentContent, post_id: postId, username }),
        });
        if (response.ok) {
            fetchPosts();
            setCommentContent('');
            setSelectedPostId(null);
        }
    };

    return (
        <div className="helpdesk-container">
            <h1>Help Desk</h1>
            <div className="add-post">
                <h2>Dodaj Post</h2>
                <input
                    type="text"
                    placeholder="Tytuł"
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                />
                <input
                    type="text"
                    placeholder="Opis"
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                />
                <input
                    type="text"
                    placeholder="Nazwa użytkownika"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />
                <button onClick={handleAddPost}>Dodaj</button>
            </div>
            <div className="posts">
                {posts.map(post => (
                    <div key={post.id} className="post">
                        <h3>{post.title}</h3>
                        <p>{post.description}</p>
                        <p>{post.username}</p>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default HelpDesk;