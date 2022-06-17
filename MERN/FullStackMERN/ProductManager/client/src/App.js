import React from 'react';
import {BrowserRouter, Routes, Route} from "react-router-dom";
import Main from "./views/Main";
import Detail from "./components/Detail";
import Update from "./components/Update";

function App() {
  return (
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Main/>}/>
          <Route path="/products/:id" element={<Detail/>} />
          <Route path="/products/edit/:id" element={<Update/>}/>
        </Routes>
      </BrowserRouter>
  );
}

export default App;
