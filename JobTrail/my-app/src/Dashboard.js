import React from 'react';
import './Dashboard.css';

function Dashboard() {
  return (
    <div className="dashboard-container">
      <div className="dashboard-header">
        <h1 className="dashboard-title">Job<span className="highlight">T</span>rail</h1>
        <div className="search-bar">
          <label className="search-label">Type in skills:</label>
          <input type="text" className="search-input" />
          <button className="search-button">Search Jobs</button>
        </div>
        <div className="upload-resume">
          <label className="resume-label">Upload resume:</label>
          <input type="file" className="resume-input" />  
          <button className="search-button">Search Jobs</button>
        </div>
      </div>

      <div className="dashboard-content">
        <p> Job listings will appear here</p>
      </div>
      <div className= "Tbutton"></div>
      <button className = "AI-button">Ask AI</button>
    </div>
  );
}

export default Dashboard;
