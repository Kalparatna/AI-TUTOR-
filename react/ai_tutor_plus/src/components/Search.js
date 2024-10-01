import React from 'react';
import { useNavigate } from 'react-router-dom';
import './Search.css';  

const Search = () => {
  const navigate = useNavigate();

  const handleSearch = () => {
    navigate('/modules'); // Navigate to the Modules page
  };

  return (
    <div className="container">
      <div className="header">
        <h1 className="title">AI Tutor Plus</h1>
      </div>
      <h2 className="subtitle">A Personalized Learning Journey</h2>
      <p className="paragraph">
        Unlock the potential of learning designed just for you! Our advanced platform offers a customized educational journey, empowering you to master topics at your own pace.
        Whether you're diving into something new or refining your skills, we're here to guide you every step of the way.
      </p>
      <p className="paragraph">
        Excited to start your learning adventure? Type in any topic and begin your exploration!
      </p>
      <div className="input-container">
        <input className="input" placeholder="Search for anything..." />
        <button className="button" onClick={handleSearch}>
          Search
        </button>
      </div>
    </div>
  );
};

export default Search;
