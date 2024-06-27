import React from 'react';
import { Link } from 'react-router-dom';

const Dashboard = () => {
    return (
        <div>
            <h2>Dashboard</h2>
            <ul>
                <li><Link to="/contracts">View Contracts</Link></li>
                <li><Link to="/messages">View Messages</Link></li>
            </ul>
        </div>
    );
};

export default Dashboard;
