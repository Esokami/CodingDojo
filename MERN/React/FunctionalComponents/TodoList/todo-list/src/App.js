import React, {useState} from 'react';
import './App.css';
import Todo from './components/Todo';
import styles from './components/Todo.module.css';

function App() {
  return(
    <div className={styles.body}>
      <Todo/>
    </div>
  );
}

export default App;
