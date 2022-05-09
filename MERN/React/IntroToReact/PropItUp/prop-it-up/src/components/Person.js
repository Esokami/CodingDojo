import React from 'react';

const Person = (props) => {
    return (
        <div>
            <h2>{ props.title }</h2>
            <p>Name: { props.name }</p>
            <p>Role: {props.role}</p>
        </div>
    )
}

export default Person;