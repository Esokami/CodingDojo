import React, {useState} from 'react';

const PersonCard = (props) => {
    const [ birthday, setBirthday ] = useState(props.age);
    return (
        <div>
            <h3>{props.lastName}, {props.firstName}</h3>
            <p>Age: {birthday}</p>
            <p>Hair Color: {props.hairColor}</p>
            <button onClick={ (event) => setBirthday(birthday + 1) }>Birthday Button for {props.firstName} {props.lastName}</button>
        </div>
    )
}

export default PersonCard;