export const addEntry = async (username, content, callback, setUsername, setContent) => {
    try {
        const response = await fetch('/api/helpdesk/add_entry', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, content })
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        callback();
        setUsername('');
        setContent('');
    } catch (error) {
        console.error('Failed to add entry:', error);
    }
};

export const loadEntries = async (setEntries) => {
    try {
        const response = await fetch('/get_entries', {
            headers: {
                'Content-Type': 'application/json'
            }
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // **Poprawka 1:** Wyloguj response.status, a nie obietnicę response.json()
        console.log('response status:', response.status);
        const contentType = response.headers.get('content-type');
        if (contentType && contentType.includes('application/json')) {
            const entries = await response.json();
            console.log('entries:', entries);
            setEntries(entries); // Dodaj ustawienie entries
        } else {
            throw new Error('Response is not in JSON format');
        }

    } catch (error) {
        console.error('Failed to load entries:', error);
        setEntries([]);
    }
};
