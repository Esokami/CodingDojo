import React from 'react';
import {BrowserRouter, Routes, Route} from "react-router-dom";
import Main from "./views/Main";
import CreateAuthor from "./components/CreateAuthor";
import UpdateAuthor from "./components/UpdateAuthor";

function App() {
  return (
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Main/>}/>
          <Route path="/authors/new" element={<CreateAuthor/>} />
          <Route path="/authors/edit/:id" element={<UpdateAuthor/>}/>
        </Routes>
      </BrowserRouter>
  );
}

export default App;
