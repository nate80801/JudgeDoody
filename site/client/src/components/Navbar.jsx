import React from 'react';
import {Link} from 'react-router-dom';

import '../styles.scss';
function Navbar() {
    return(
        <div className='navbar'>
            <div className='container'>
                <div className='main'>
                    <Link to='/'><h1>judgedoody</h1></Link>
                </div>
                <div className='links'>
                    <Link class='link' to='/docs'><h4>documentation</h4></Link>
                    <Link class='link' to='/about'><h4>about</h4></Link>
                    <button><a href="">invite</a></button>
                </div>
            </div>
        </div>
    );
}

export default Navbar;