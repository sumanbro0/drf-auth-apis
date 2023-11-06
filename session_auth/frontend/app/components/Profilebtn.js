'use client'
import Link from 'next/link';
import { useSession } from '../hooks/useSession';
import { useEffect, useState } from 'react';
const Profilebtn = () => {
    const isAuthenticated = useSession((state) => state.isAuthenticated)
    const [loading, setLoading] = useState(true)
    const logout = useSession((state) => state.unAuthenticate)
    const handleClick = async (e) => {
        e.preventDefault();
        const response = await fetch('http://127.0.0.1:8000/api/logout', {
            method: 'GET',
            credentials: 'include',
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
        })
        const data = await response.json()
        console.log(data)
        logout();
    }

    useEffect(() => {
        setLoading(false)
    }, []);

    if (loading) return null
    return (
        <div>
            {!isAuthenticated ? <div className="w-auto block">
                <Link href={'/login'} >
                    <button
                        className="inline-block text-sm px-4 py-2 leading-none border rounded text-white border-white hover:border-transparent hover:text-blue-500 hover:bg-white mt-4 lg:mt-0"
                    >
                        Login
                    </button>
                </Link>
                <Link href={'/signup'} >

                    <button
                        className="inline-block ml-8 text-sm px-4 py-2 leading-none border rounded text-white border-white hover:border-transparent hover:text-blue-500 hover:bg-white mt-4 lg:mt-0"
                    >
                        Signup
                    </button>
                </Link>

            </div> :
                <div className='cursor-pointer'>
                    <h1 onClick={handleClick}>profile</h1>
                </div>

            }
        </div>
    )
}

export default Profilebtn