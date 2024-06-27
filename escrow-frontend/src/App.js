import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './components/Login';
import Dashboard from './components/Dashboard';
import Contracts from './components/Contracts';
import ContractDetails from './components/ContractDetails';
import Messages from './components/Messages';

const App = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Login />} />
                <Route path="/dashboard" element={<Dashboard />} />
                <Route path="/contracts" element={<Contracts />} />
                <Route path="/contracts/:id" element={<ContractDetails />} />
                <Route path="/messages" element={<Messages />} />
            </Routes>
        </Router>
    );
};

export default App;
