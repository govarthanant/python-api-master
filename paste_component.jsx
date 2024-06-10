import React, { useState } from 'react';

const PasteCaptureComponent = () => {
    const [pastedText, setPastedText] = useState('');

    // Function to handle the paste event
    const handlePaste = async (event) => {
        // Prevent the default paste behavior
        event.preventDefault();

        // Get the pasted data
        const paste = (event.clipboardData || window.clipboardData).getData('text');
        setPastedText(paste);

        // Call the backend API with the pasted data
        await callBackendAPI(paste);
    };

    // Function to call the backend API
    const callBackendAPI = async (text) => {
        try {
            const response = await fetch('https://your-backend-api-endpoint.com/endpoint', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ data: text }),
            });

            const result = await response.json();
            console.log('API response:', result);
        } catch (error) {
            console.error('Error calling backend API:', error);
        }
    };

    return (
        <div>
            <h1>Paste Capture Component</h1>
            <input
                type="text"
                placeholder="Paste something here"
                onPaste={handlePaste}
            />
            <p>Pasted Text: {pastedText}</p>
        </div>
    );
};

export default PasteCaptureComponent;
