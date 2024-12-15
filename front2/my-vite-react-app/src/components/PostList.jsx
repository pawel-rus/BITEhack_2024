import React, { useEffect, useState } from 'react';

const PostList = () => {
    const [posts, setPosts] = useState([]);
    const [error, setError] = useState('');

    useEffect(() => {
        const fetchPosts = async () => {
            try {
                const response = await fetch('/api/helpdesk/posts');
                if (response.ok) {
                    const data = await response.json();
                    setPosts(data);
                } else {
                    const errorData = await response.json();
                    setError(errorData.error || 'Wystąpił błąd podczas pobierania postów');
                }
            } catch (error) {
                setError('Wystąpił błąd podczas komunikacji z serwerem');
            }
        };
        fetchPosts();
    }, []);

    return (
        <div>
            {error && <div style={{ color: 'red' }}>{error}</div>}
            <ul>
                {posts.map((post) => (
                    <li key={post.id}>
                        <strong>{post.nick}:</strong> {post.content}
                        <br />
                        <small>Data: {post.date}</small>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default PostList;