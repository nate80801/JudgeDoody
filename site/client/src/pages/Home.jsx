import React from 'react';
import '../styles.scss';
import judge from '../assets/judge.jpg';
import graphic from '../assets/graphic.jpg';

function Home() {
    return(
        <div className='home'>
            <div className='main'>
                <div className='hero'>
                    <h1>A striking voice of reason when you need it.</h1>
                    <button type='button'><h2>Invite JudgeDoody</h2></button>
                </div>
                <div className='logo'>
                    <img src={graphic} alt="judge graphic" />
                </div>
            </div>
            <div className='body'>
                <h1>a bot that serves justice</h1>
            </div>
        </div>
    );
}

export default Home;