import React, {useState} from 'react';
import styles from './Tab.module.css';

const Tab = (props) => {
    const {currentTab, setCurrentTab, tabContent} = props;

    return (
        <div className={styles.container}>
            <div className={styles.tab}>
                <button className={styles.btn} onClick={() => setCurrentTab(0)}>Dragon Age</button>
                <button className={styles.btn} onClick={() => setCurrentTab(1)}>The Elder Scrolls</button>
                <button className={styles.btn} onClick={() => setCurrentTab(2)}>The Witcher</button>
            </div>
            <div className={styles.tab}>
                <textarea row="6" cols="40" value={tabContent[currentTab].text}></textarea>
            </div>
        </div>
    )
}

export default Tab;