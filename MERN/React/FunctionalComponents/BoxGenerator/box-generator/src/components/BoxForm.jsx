import React, {Component, useState} from 'react';
import BoxDisplay from './BoxDisplay';
import styles from './BoxComponent.module.css';

const BoxForm = (props) => {
    const [box, setBox] = useState("");
    const [boxArr, setBoxArr] = useState([]);

    const handleSubmit = (e) => {
        e.preventDefault();
        
        const newBoxObj = {
            box : box,
        }

        const newBoxArr = [...boxArr, newBoxObj];
        setBoxArr(newBoxArr);
        setBox("");
    }

    return (
        <div>
        <form onSubmit={handleSubmit}>
            <label>Color</label>
            <input type="text" onChange={(e) => setBox(e.target.value)} value={box}></input>
            <button type="submit">Add</button>
        </form>

        {boxArr.map((n, index) => {
            return (
                <div className={styles.box} key={index}>
                    <p><BoxDisplay bgColor={n.box}/></p>
                </div>
            )
        })}
        </div>
    )
}

export default BoxForm;