
import React, { useState } from 'react';

function HealthChat() {
    const [prompt, setPrompt] = useState('');
    const [response, setResponse] = useState('');
    const [loading, setLoading] = useState(false);

    const handleGenerate = async () => {
        setLoading(true);
        try {
            const res = await fetch('/api/generate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ prompt })
            });
            const data = await res.json();
            setResponse(data.response || "No response received.");
        } catch (error) {
            setResponse("Error fetching response.");
        }
        setLoading(false);
    };

    return (
        <div>
            <h2>Ask Health Assistant</h2>
            <textarea value={prompt} onChange={e => setPrompt(e.target.value)} placeholder="Ask your health question..." />
            <button onClick={handleGenerate} disabled={loading}>
                {loading ? "Generating..." : "Ask"}
            </button>
            <div>
                <h3>Response:</h3>
                <p>{response}</p>
            </div>
        </div>
    );
}

export default HealthChat;
                    