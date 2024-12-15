import React, { useState, useEffect } from "react";
import axios from "axios";

function Comments({ thread, goBack }) {
    const [comments, setComments] = useState([]);
    const [newCommentText, setNewCommentText] = useState("");

    // Pobierz komentarze
    useEffect(() => {
        fetchComments();
    }, []);

    const fetchComments = async () => {
        const response = await axios.get(
            `http://127.0.0.1:5001/threads/${thread.id}/comments`,
            { headers: { Authorization: `Bearer ${localStorage.getItem("token")}` } }
        );
        setComments(response.data);
    };

    const handleAddComment = async () => {
        if (!newCommentText.trim()) return;
        await axios.post(
            `http://127.0.0.1:5001/threads/${thread.id}/comments`,
            { text: newCommentText },
            { headers: { Authorization: `Bearer ${localStorage.getItem("token")}` } }
        );
        setNewCommentText("");
        fetchComments();
    };

    return (
        <div>
            <h2>{thread.title}</h2>
            <button onClick={goBack}>Back</button>
            <ul>
                {comments.map((comment) => (
                    <li key={comment.id}>
                        <strong>{comment.user_id}</strong>: {comment.text}
                    </li>
                ))}
            </ul>
            <textarea
                placeholder="Write a comment..."
                value={newCommentText}
                onChange={(e) => setNewCommentText(e.target.value)}
            />
            <button onClick={handleAddComment}>Add Comment</button>
        </div>
    );
}

export default Comments;
