import React, { useState } from 'react';
import { useLocation } from 'react-router-dom';
import './Chat.css'; 

const Chat = () => {
  const [message, setMessage] = useState('');
  const location = useLocation();
  const { tutor } = location.state || {}; // Get the selected tutor from the location state

  const handleSend = () => {
    console.log('Message sent:', message);
    setMessage(''); // Clear the message input
  };

  return (
    <div className="chat-container">
      <div className="sidebar">
        <ul>
          <li>Generated Modules will appear here</li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
        </ul>
      </div>
      <div className="chat-section">
        {/* Display the selected tutor's name instead of "SRK" */}
        <h2>Learn from {tutor || 'your selected tutor'} about { }</h2>
        <textarea
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Type your message..."
        ></textarea>
        <div className="button-container">
          <button onClick={handleSend}>Send</button>
          <button>Clear Chat</button>
          <button>Export Chat</button>
          <button>Finish</button>
        </div>
      </div>
    </div>
  );
};

export default Chat;
