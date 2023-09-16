import React from 'react';
import headshot from '../assets/headshot.jpg';
import darren from '../assets/darren1.jpg';
import nathan from '../assets/nathan.png';
import github from '../assets/github-mark/github-mark.png';
import linkedin from '../assets/LinkedIn-Logos/LI-In-Bug.png';

function About() {
    return(
        <div className='about'>
            <div className='main'>
                <h1>Created by a team that seeks justice <br></br>for all discord users</h1>
                <p>We know how it feels to get accused of the most awful, heinous, preposterous things when <br></br>on a call with friends on Discord. A word slips
                    out and suddenly you have a 1st degree felony.<br></br> JudgeDoody is there to serve swift and fair justice to those unrepresented in a voice channel.
                </p>
            </div>
            <div className='team'>
                <div className='member'>
                    <div className='nathanHead'>
                        <img src={nathan} alt="headshot" />
                    </div>
                    <div className='description'>
                        <h2>Nathan Do</h2>
                        <span>Bot Developer</span>
                        <div className='icons'>
                            <a href="https://github.com/nate80801"><img style={{width: 30}}src={github} alt="github icon" /></a>
                            <a href="https://www.linkedin.com/in/nathan-do-b43461253/"><img style={{width: 30}}src={linkedin} alt="linkedin logo" /></a>
                        </div>
                    </div>
                </div>
                <div className='member'>
                    <div className='darrenHead'>
                        <img src={darren} alt="headshot" />
                    </div>
                    <div className='description'>
                        <h2>Darren Bansil</h2>
                        <span>Web Developer</span>
                        <div className='icons'>
                            <a href="https://github.com/libioco"><img style={{width: 30}}src={github} alt="github icon" /></a>
                            <a href="https://www.linkedin.com/in/darrenbansil/"><img style={{width: 30}}src={linkedin} alt="linkedin logo" /></a>
                        </div>
                    </div>
                </div>
                <div className='member'>
                    <div className='dannyHead'>
                        <img src={headshot} alt="headshot" />
                    </div>
                    <div className='description'>
                        <h2>Daniel Gomez</h2>
                        <span>Bot Developer</span>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default About;