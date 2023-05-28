import React from 'react';
import './styles.css';

function App() {
  return (
    <div className="container">
      <div className="header">
        <h1>Job<span className="highlight">T</span>rail</h1>
      </div>

      <div className="form-container">
        <h2>Login</h2>
        <form>
          <div className="form-group">
            <input type="email" id="email" name="email" placeholder="Email" />
          </div>

          <div className="form-group">
            <input type="password" id="password" name="password" placeholder="Password" />
          </div>

          <button type="submit">Login</button>
        </form>

        <h2>Sign Up</h2>
        <form>
          <div className="form-group">
            <input type="email" id="email" name="email" placeholder="Email" />
          </div>

          <div className="form-group">
            <input type="password" id="password" name="password" placeholder="Password" />
          </div>

          <button type="submit">Sign Up</button>
        </form>
      </div>
    </div>
  );
}

export default App;

