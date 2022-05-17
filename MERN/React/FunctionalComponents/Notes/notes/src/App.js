import React, {useState} from 'react';
import './App.css';
import MyNewComponent from './components/MyNewComponent';
import Groceries from './components/Grociers';
import MyButton from './components/MyButtonComponent';
import MessageForm from './components/MessageForm';
import MessageDisplay from './components/MessageDisplay';

function App() {
  // Lifting State includes creating it in a common parent that can pass data down to All
  // components that will need access to the getter, setter or both

  const [currentMsg, setCurrentMsg] = useState("There are no messages");

  const youveGotMail = (newMessage) => {
    setCurrentMsg(newMessage);
  }
  return (
    // <div className="App">
    //   <MyNewComponent header={ "Header Prop" }>
    //     <h1>These are children</h1>
    //     <p>This is a child</p>
    //     <p>This is another child</p>
    //     <p>This is another nother child</p>
    //   </MyNewComponent>
    //   <MyButton/>
    //   <Groceries/>
    // </div>
      <>
        <MessageForm onNewMessage={youveGotMail}/>
        <MessageDisplay message={currentMsg} />
      </>
  )
}

export default App;