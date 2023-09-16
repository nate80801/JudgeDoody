import React from 'react';
import {Link} from 'react-router-dom';

import '../styles.scss';
function Navbar() {
    return(
        <div className='navbar'>
            <div className='container'>
                <div className='main'>
                    <Link to='/'><h1>JudgeDoody</h1></Link>
                </div>
                <div className='links'>
                    <Link class='link' to='/docs'><h4>Documentation</h4></Link>
                    <Link class='link' to='/about'><h4>About</h4></Link>
                    <Link>Invite Link</Link>
                </div>
            </div>
        </div>
    );
}

export default Navbar;