import React, { useState, useEffect } from 'react';

const Profile = () => {
    const [profile, setProfile] = useState({});

    useEffect(() => {
        const fetchProfile = async () => {
            const response = await fetch('http://localhost:5000/main/profile', {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('token')}`
                }
            });
            const data = await response.json();
            setProfile(data);
        };
        fetchProfile();
    }, []);

    return (
        <div>
            <h2>Profile</h2>
            <p>Username: {profile.username}</p>
        </div>
    );
};

export default Profile;
