import React from 'react';
import './App.css';
import FileUpload from './components/FileUpload';
import FileList from './components/FileList';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Cloud File Storage</h1>
      </header>
      <main>
        <FileUpload />
        <FileList />
      </main>
    </div>
  );
}

export default App;
