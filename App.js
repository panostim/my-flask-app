import React, { useState, useEffect } from "react";
import "./App.css";

function App() {
    const [time, setTime] = useState(new Date());
    const [serverTimestamp, setServerTimestamp] = useState("");
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        const interval = setInterval(() => {
            setTime(new Date());
        }, 1000);

        return () => clearInterval(interval);
    }, []);

    useEffect(() => {
        const fetchTimestamp = async () => {
            try {
                const response = await fetch("/api/timestamp");
                const data = await response.json();
                setServerTimestamp(data.timestamp);
                setIsLoading(false);
            } catch (error) {
                console.error("Error fetching timestamp:", error);
                setIsLoading(false);
            }
        };

        fetchTimestamp();
        const serverInterval = setInterval(fetchTimestamp, 1000);

        return () => clearInterval(serverInterval);
    }, []);

    const formatTime = (date) => {
        return date.toLocaleTimeString('en-US', {
            hour12: false,
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit'
        });
    };

    const formatDate = (date) => {
        return date.toLocaleDateString('en-US', {
            weekday: 'long',
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        });
    };

    return (
        <div className="app">
            <div className="background">
                <div className="gradient-overlay"></div>
                <div className="floating-shapes">
                    <div className="shape shape-1"></div>
                    <div className="shape shape-2"></div>
                    <div className="shape shape-3"></div>
                </div>
            </div>
            
            <div className="container">
                <header className="header">
                    <h1 className="title">
                        <span className="title-icon">⏰</span>
                        Time & Date
                    </h1>
                    <p className="subtitle">Real-time synchronization with server</p>
                </header>

                <div className="content">
                    <div className="time-section">
                        <div className="time-card">
                            <div className="card-header">
                                <span className="card-icon">🕐</span>
                                <h2>Current Time</h2>
                            </div>
                            <div className="time-display">
                                {formatTime(time)}
                            </div>
                        </div>

                        <div className="date-card">
                            <div className="card-header">
                                <span className="card-icon">📅</span>
                                <h2>Current Date</h2>
                            </div>
                            <div className="date-display">
                                {formatDate(time)}
                            </div>
                        </div>
                    </div>

                    <div className="timestamp-section">
                        <div className="timestamp-card">
                            <div className="card-header">
                                <span className="card-icon">⚡</span>
                                <h2>ISO Timestamp</h2>
                            </div>
                            <div className="timestamp-display">
                                {time.toISOString()}
                            </div>
                        </div>

                        <div className="server-card">
                            <div className="card-header">
                                <span className="card-icon">🌐</span>
                                <h2>Server Timestamp</h2>
                            </div>
                            <div className="server-display">
                                {isLoading ? (
                                    <div className="loading">
                                        <div className="spinner"></div>
                                        <span>Connecting...</span>
                                    </div>
                                ) : (
                                    serverTimestamp || "Not available"
                                )}
                            </div>
                        </div>
                    </div>
                </div>

                <footer className="footer">
                    <p>Built with React & Flask</p>
                    <div className="tech-stack">
                        <span className="tech-badge">React</span>
                        <span className="tech-badge">Flask</span>
                        <span className="tech-badge">API</span>
                    </div>
                </footer>
            </div>
        </div>
    );
}

export default App;
