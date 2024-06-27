import React from 'react';
import { useParams } from 'react-router-dom';

const ContractDetails = () => {
    const { id } = useParams();
    // Fetch contract details using the id
    const contract = { id, name: `Contract ${id}`, details: 'Contract details here...' };

    return (
        <div>
            <h2>{contract.name}</h2>
            <p>{contract.details}</p>
        </div>
    );
};

export default ContractDetails;
