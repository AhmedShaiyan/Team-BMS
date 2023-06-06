import React, { useState } from 'react';


import Login from './LoginForm';
import Dashboard from './Dashboard';

function App() {
  const [isLoggedIn, setLoggedIn] = useState(false);

  const handleLogin = () => {
    setLoggedIn(true);
  };

  return (
    <div className="App">
      {isLoggedIn ? (
        <Dashboard />
      ) : (
        <Login onLogin={handleLogin} />
      )}
    </div>
  );
}

export default App;
