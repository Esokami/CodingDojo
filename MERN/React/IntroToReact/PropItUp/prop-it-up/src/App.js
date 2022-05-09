import React from 'react';
import './App.css';
import Person from './components/Person';
import PersonCard from './components/PersonCard';

function App() {
  return (
    <div className="App">
      <PersonCard 
        firstName={"Geralt"}
        lastName={"Rivia"}
        age={45}
        hairColor={"White"}/>
        <PersonCard 
        firstName={"Yennefer"}
        lastName={"Vengerberg"}
        age={45}
        hairColor={"Black"}/>
        <PersonCard 
        firstName={"Cirilla"}
        lastName={"Riannon"}
        age={18}
        hairColor={"White"}/>
        <PersonCard 
        firstName={"Julian"}
        lastName={"Pankratz"}
        age={40}
        hairColor={"Brown"}/>
    </div>
  );
}

export default App;
