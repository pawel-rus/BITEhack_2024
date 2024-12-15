import React, { useState, useCallback } from 'react';
import PostForm from './PostForm';
import PostList from './PostList';

function AssistantContent() {
    const [postAdded, setPostAdded] = useState(false)
    const handlePostAdded = useCallback(() => {
        setPostAdded(prev => !prev)
    }, [])

    return (
        <div>
            <h1>Forum</h1>
            <PostForm onPostAdded={handlePostAdded} />
            <PostList key={postAdded} />
        </div>
    );
}

export default AssistantContent;