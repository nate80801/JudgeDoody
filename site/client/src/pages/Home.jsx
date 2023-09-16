import React from 'react';
import '../styles.scss';
import judge from '../assets/judge.jpg';
import graphic from '../assets/graphic.jpg';
import {TypeAnimation} from 'react-type-animation';

function Home() {
    return(
        <div className='home'>
            <div className='main'>
                <div className='hero'>
                    <TypeAnimation
                        sequence={[
                            'A striking voice of reason when you need it.'
                        ]}
                        wrapper="span"
                        speed={50}
                        style={{ fontSize: 50, fontWeight: 300, textAlign: 'center'}}
                        repeat={1}
                        />
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