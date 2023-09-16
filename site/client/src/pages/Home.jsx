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
                        speed={25}
                        style={{ fontSize: 50, fontWeight: 300, textAlign: 'center'}}
                        repeat={0}
                        />
                    <button type='button'><a href="https://discord.com/api/oauth2/authorize?client_id=1152453723591823422&permissions=68164943608512&scope=bot"><h2>Invite JudgeDoody</h2></a></button>
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