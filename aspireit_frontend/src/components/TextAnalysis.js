import React, { useState } from 'react';

const TextAnalysis = () => {
    const [text, setText] = useState('');
    const [polarity, setPolarity] = useState(null);

    const handleAnalysis = async () => {
        const response = await fetch('http://localhost:5000/main/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                Authorization: `Bearer ${localStorage.getItem('token')}`
            },
            body: JSON.stringify({ text })
        });
        const data = await response.json();
        setPolarity(data.polarity);
    };

    return (
        <div>
            <h2>Text Analysis</h2>
            <textarea
                placeholder="Enter text..."
                value={text}
                onChange={(e) => setText(e.target.value)}
            />
            <button onClick={handleAnalysis}>Analyze</button>
            {polarity !== null && (
                <p>Polarity: {polarity}</p>
            )}
        </div>
    );
};

export default TextAnalysis;
