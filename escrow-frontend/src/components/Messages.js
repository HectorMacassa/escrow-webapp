import React from 'react';

const Messages = () => {
    // This is just a sample data
    const messages = [
        { id: 1, sender: 'User 1', text: 'Message 1' },
        { id: 2, sender: 'User 2', text: 'Message 2' }
    ];

    return (
        <div>
            <h2>Messages</h2>
            <ul>
                {messages.map(message => (
                    <li key={message.id}>
                        <p><strong>{message.sender}:</strong> {message.text}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Messages;
