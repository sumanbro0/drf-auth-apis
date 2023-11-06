'use client'

import React, { useState } from 'react';

const Signup = () => {
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleUsernameChange = (e) => {
        setUsername(e.target.value);
    };

    const handleEmailChange = (e) => {
        setEmail(e.target.value);
    };

    const handlePasswordChange = (e) => {
        setPassword(e.target.value);
    };


    const handleSubmit = async (e) => {
        e.preventDefault();

        const userData = {
            username: username,
            email: email,
            password: password,
        };

        try {
            const response = await fetch('http://127.0.0.1:8000/api/register/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(userData),
            });

            if (!response.ok) {
                if (response.status === 400) { // 409 for conflict, assuming it's a duplicate username
                    const errorData = await response.json();
                    if (errorData.username) {
                        throw new Error('A user with that username already exists.');
                    } else {
                        throw new Error('Login failed');
                    }
                } else {
                    throw new Error('Login failed');
                }
            }

            const data = await response.json();
            console.log('Login successful!', data);


            setUsername('');
            setEmail('');
            setPassword('');
        } catch (error) {
            console.error('Error:', error);
            alert(error)
        }
    };

    return (
        <div className="max-w-md mx-auto">
            <h2 className="text-3xl font-bold mb-4">Signup</h2>
            <form onSubmit={handleSubmit} className="space-y-4">
                <input type="text" placeholder="Username" value={username} onChange={handleUsernameChange} className="w-full text-black border rounded-md p-2" />
                <input type="email" placeholder="Email" value={email} onChange={handleEmailChange} className="w-full text-black border rounded-md p-2" />
                <input type="password" placeholder="Password" value={password} onChange={handlePasswordChange} className="w-full text-black border rounded-md p-2" />
                <button type="submit" className="w-full bg-blue-500 text-white font-bold py-2 rounded-md">Sign Up</button>
            </form>
        </div>
    );
};

export default Signup;
