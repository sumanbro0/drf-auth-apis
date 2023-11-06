'use client'

import React, { useState, useEffect } from 'react';
import { useSession } from '../hooks/useSession';
import { redirect } from 'next/navigation';
import axios from 'axios';
axios.defaults.withCredentials = true
const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const login = useSession((state) => state.authenticate)
    const handleUsernameChange = (e) => {
        setUsername(e.target.value);
    };

    const handlePasswordChange = (e) => {
        setPassword(e.target.value);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        const userData = {
            username: username,
            password: password,
        };

        try {
            const response = await axios.post('http://127.0.0.1:8000/api/login/', userData, {
                headers: {
                    'Content-Type': 'application/json',
                }
            });

            // Handle the response here
            console.log(response.data);

            if (!response) {
                const errorData = response;
                if (errorData.null && errorData.required && errorData.invalid) {
                    throw new Error('Invalid Credentials');
                }
                console.log(errorData)
                throw new Error('Login failed');
            }

            login();
            console.log('Login successful!', response.data);


            setUsername('');
            setPassword('');
            // window.location.replace('/home')
        } catch (error) {
            console.error('Error:', error);
            alert(error)
        }
    };

    return (
        <div className="max-w-md mx-auto">
            <h2 className="text-3xl font-bold mb-4">Login</h2>
            <form onSubmit={handleSubmit} className="space-y-4">
                <input type="text" placeholder="Username" value={username} onChange={handleUsernameChange} className="w-full text-black border rounded-md p-2" />
                <input type="password" placeholder="Password" value={password} onChange={handlePasswordChange} className="w-full text-black border rounded-md p-2" />
                <button type="submit" className="w-full bg-blue-500 text-white font-bold py-2 rounded-md">Login</button>
            </form>
        </div>
    );
};

export default Login;
