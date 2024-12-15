import React, { useState, useEffect } from "react";
import axios from "axios";
import Comments from "./Comments";

function ThreadList() {
    const [threads, setThreads] = useState([]);
    const [newThreadTitle, setNewThreadTitle] = useState("");
    const [selectedThread, setSelectedThread] = useState(null);

    // Pobierz wątki z backendu
    useEffect(() => {
        fetchThreads();
    }, []);

    const fetchThreads = async () => {
        const response = await axios.get("http://127.0.0.1:5001/threads", {
            headers: { Authorization: `Bearer ${localStorage.getItem("token")}` },
        });
        setThreads(response.data);
    };

    const handleAddThread = async () => {
        if (!newThreadTitle.trim()) return;
        await axios.post(
            "http://127.0.0.1:5001/threads",
            { title: newThreadTitle },
            { headers: { Authorization: `Bearer ${localStorage.getItem("token")}` } }
        );
        setNewThreadTitle("");
        fetchThreads();
    };

    if (selectedThread) {
        return (
            <Comments
                thread={selectedThread}
                goBack={() => setSelectedThread(null)}
            />
        );
    }

    return (
        <div>
            <h2>Threads</h2>
            <ul>
                {threads.map((thread) => (
                    <li key={thread.id} onClick={() => setSelectedThread(thread)}>
                        {thread.title}
                    </li>
                ))}
            </ul>
            <input
                type="text"
                placeholder="New thread title"
                value={newThreadTitle}
                onChange={(e) => setNewThreadTitle(e.target.value)}
            />
            <button onClick={handleAddThread}>Add Thread</button>
        </div>
    );
}

export default ThreadList;
