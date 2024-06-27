import React from 'react';
import { Link } from 'react-router-dom';

const Contracts = () => {
    // This is just a sample data
    const contracts = [
        { id: 1, name: 'Contract 1' },
        { id: 2, name: 'Contract 2' }
    ];

    return (
        <div>
            <h2>Contracts</h2>
            <ul>
                {contracts.map(contract => (
                    <li key={contract.id}>
                        <Link to={`/contracts/${contract.id}`}>{contract.name}</Link>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Contracts;
