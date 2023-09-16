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
                            'A bot for the villains.',
                            1000,
                            'A bot for the menaces.',
                            1000,
                            'A bot for the goblins.',
                            1000,
                            'A bot for the unhinged.',
                            1000,
                        ]}
                        wrapper="span"
                        speed={50}
                        style={{ fontSize: 50, fontWeight: 300, textAlign: 'center'}}
                        repeat={1}
                        />
                    <button type='button'><h3>Invite JudgeDoody</h3></button>
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