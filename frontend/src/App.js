import React from 'react';
import logo from './logo.svg';
import './App.css';
import axios from "axios";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />

        {testAxios()}
      </header>
    </div>
  );
}

function testAxios() {
  axios.get("/api/collections")
    .then(res => console.log(res));
}

export default App;
