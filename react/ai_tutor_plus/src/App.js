import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Search from './components/Search';
import Charecter from './components/Charecter';
import Modules from './components/Modules';
import Chat from './components/Chat'; // Import Chat component

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Search />} />
        <Route path="/modules" element={<Modules />} />
        <Route path="/choose-tutor" element={<Charecter />} />
        <Route path="/chat" element={<Chat />} /> {/* Add route for chat interface */}
      </Routes>
    </Router>
  );
};

export default App;
