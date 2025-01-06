import React, { useState, useEffect } from "react";

function App() {
    const [time, setTime] = useState(new Date());
    const [serverTimestamp, setServerTimestamp] = useState("");

    useEffect(() => {
        const interval = setInterval(() => {
            setTime(new Date());
        }, 1000);

        return () => clearInterval(interval);
    }, []);

    useEffect(() => {
        const fetchTimestamp = async () => {
            try {
                const response = await fetch("https://your-backend-url/api/timestamp");
                const data = await response.json();
                setServerTimestamp(data.timestamp);
            } catch (error) {
                console.error("Error fetching timestamp:", error);
            }
        };

        fetchTimestamp();
        const serverInterval = setInterval(fetchTimestamp, 1000);

        return () => clearInterval(serverInterval);
    }, []);

    return (
        <div style={{ textAlign: "center", padding: "20px" }}>
            <h1>React Time & Date</h1>
            <p>Current Time: {time.toLocaleTimeString()}</p>
            <p>Current Date: {time.toLocaleDateString()}</p>
            <p>Timestamp: {time.toISOString()}</p>
            <p>Server Timestamp: {serverTimestamp}</p>
        </div>
    );
}

export default App;
