import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Charecter.css';  

const Charecter = () => {
  const [selectedTutor, setSelectedTutor] = useState(null);
  const navigate = useNavigate();

  const tutors = [
    {
      name: 'Virat Kohli',
      description: 'Virat Kohli, a world-renowned cricketer, is known for his leadership, discipline, and relentless drive for excellence.',
      image: '/images/image12.jpg' 
    },
    {
      name: 'Doraemon',
      description: 'Doraemon is a helpful robotic cat from the future, always ready with futuristic gadgets to solve any problem.',
      image: '/images/image22.jpg'
    },
    {
      name: 'SRK',
      description: 'Shah Rukh Khan, the King of Bollywood, is known for his charisma, wit, and resilience.',
      image: '/images/image42.jpg'
    },
    {
      name: 'Steve Jobs',
      description: 'Steve Jobs, a visionary and innovator, co-founded Apple and revolutionized the tech industry.',
      image: '/images/image32.jpg'
    }
  ];

  const handleSubmit = () => {
    if (selectedTutor) {
      navigate('/chat', { state: { tutor: selectedTutor } }); // Pass the selected tutor's name via state
    } else {
      alert('Please select a tutor before submitting.');
    }
  };

  const handleCardClick = (name) => {
    setSelectedTutor(name);
  };

  return (
    <div className="container">
      <div className="header">
        <h1 className="title">AI Tutor Plus</h1>
      </div>
      <h2 className="subtitle">Choose your AI tutor</h2>
      {tutors.map((tutor, index) => (
        <div key={index} className="tutor-card" onClick={() => handleCardClick(tutor.name)}>
          <img src={tutor.image} alt={tutor.name} className="tutor-image" />
          <div className="tutor-info">
            <h3 className="tutor-name">{tutor.name}</h3>
            <p className="tutor-description">{tutor.description}</p>
          </div>
          <input 
            type="radio" 
            name="tutor" 
            value={tutor.name} 
            onChange={() => setSelectedTutor(tutor.name)}
            checked={selectedTutor === tutor.name}
            style={{ marginLeft: '10px' }} 
          />
        </div>
      ))}
      <button className="submit-button" onClick={handleSubmit}>
        Submit
      </button>
    </div>
  );
};

export default Charecter;
