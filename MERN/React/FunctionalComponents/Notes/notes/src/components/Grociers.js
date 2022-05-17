import React from 'react';

const Groceries = (props) => {
    const groceryList = ["green onion", "garlic", "bok choy", "lime"];
    return (
        <ul>
        {
            groceryList.map( (item, index) =>
                <li key={index}>{item}</li>
                )
        }
        </ul>
    )
}

export default Groceries;