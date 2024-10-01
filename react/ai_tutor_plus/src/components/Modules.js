import React from 'react';
import { useNavigate } from 'react-router-dom';
import './Modules.css'; // Create a CSS file for styling if needed

const Modules = () => {
  const navigate = useNavigate();

  const handleNext = () => {
    navigate('/choose-tutor');
  };

  return (
    <div className="container">
      <div className="header">
        <h1 className="title">AI Tutor Plus</h1>
      </div>
      <h2 className="subtitle">Generated Modules</h2>
      <p className="paragraph">Generated modules will show here...</p>
      <button className="button" onClick={handleNext}>
        Next: Choose Tutor
      </button>
    </div>
  );
};

export default Modules;
