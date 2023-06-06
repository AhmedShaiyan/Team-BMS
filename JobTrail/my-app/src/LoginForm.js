import React, { useState } from 'react';
import'./login.css';

function Login({ onLogin }) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Perform basic dummy authentication
    if (email && password) {
      onLogin();
    }
  };

  return (
    <div className="container">
      <div className="header">
        <h1>
          Job<span className="highlight">T</span>rail
        </h1>
      </div>

      <div className="form-container">
        <h2>Login</h2>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <input
              type="email"
              id="email"
              name="email"
              placeholder="Email"
              value={email}
              onChange={handleEmailChange}
            />
          </div>

          <div className="form-group">
            <input
              type="password"
              id="password"
              name="password"
              placeholder="Password"
              value={password}
              onChange={handlePasswordChange}
            />
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

export default Login;

