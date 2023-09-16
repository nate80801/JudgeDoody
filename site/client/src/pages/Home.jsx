import React from 'react';
import '../styles.scss';
import judge from '../assets/judge.jpg';

function Home() {
    return(
        <div className='home'>
            <div className='main'>
                <div className='hero'>
                    <h1>a striking voice of reason when you need it.</h1>
                    <button type='button'><h2>add to server</h2></button>
                </div>
                <div className='logo'>
                    random image
                </div>
            </div>
            <div className='body'>
                <h1>a bot that serves justice</h1>
            </div>
        </div>
    );
}

export default Home;