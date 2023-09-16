import { useState } from 'react'
import './App.css'
import Navbar from './components/Navbar';
import About from './pages/About';
import Docs from './pages/Docs';
import Home from './pages/Home';
import {
    createBrowserRouter,
    RouterProvider,
    Outlet,
  } from "react-router-dom";

import './styles.scss';

const Layout = () => {
    return (
        <>
            <Navbar/>
            <Outlet/>
        </>
    );
};

const router = createBrowserRouter([
    {
        path: "/",
        element: <Layout/>,
        children: [
            {
                path: "/",
                element: <Home/>
            },
            {
                path: "/about",
                element: <About/>
            },
            {
                path: "/docs",
                element: <Docs/>
            },
        ]
    }
]);

function App() {
  return (
    <div class='app'>
        <div class='container'>
            <RouterProvider router={router}/>
        </div>
        
    </div>
  )
}

export default App;
