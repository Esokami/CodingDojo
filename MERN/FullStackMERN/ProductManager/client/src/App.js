import React from 'react';
import {BrowserRouter, Routes, Route} from "react-router-dom";
import Main from "./views/Main";
import Detail from "./components/Detail";
import Update from "./components/Update";

function App() {
  return (
      <BrowserRouter>
        <Routes>
          <Route element={<Main/>} path="/"/>
          <Route element={<Detail/>} path="/products/:id"/>
          <Route element={<Update/>} path="/products/edit/:id"/>
        </Routes>
      </BrowserRouter>
  );
}

export default App;
