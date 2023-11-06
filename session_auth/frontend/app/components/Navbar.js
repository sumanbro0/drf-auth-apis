'use client'

import Profilebtn from "./Profilebtn";

const Navbar = () => {

    return (
        <nav className=" mb-40 flex items-center justify-between flex-wrap bg-blue-500 p-4">
            <div className="flex items-center flex-shrink-0 text-white mr-6">
                <span className="font-semibold text-xl tracking-tight">My App</span>
            </div>
            <Profilebtn />


        </nav>
    );
};

export default Navbar;