import React, { useState } from 'react';
import './App.css';
import Tab from './components/Tab';
import styles from './components/Tab.module.css';

function App() {

  const [currentTab, setCurrentTab] = useState(0);

  const tabContent = [
    {text: 'RPG series with outstanding story and rich characters.'},
    {text: 'RPG series with outstanding story and gameplay.'},
    {text: 'RPG series with outstanding story, rich characters, and gameplay.'}
  ];

  return (
    <div className={styles.container}>
      <Tab
        setCurrentTab={setCurrentTab} tabContent={tabContent} currentTab={currentTab}
        />
    </div>
  );
}

export default App;
