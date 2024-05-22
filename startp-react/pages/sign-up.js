import React, { useState } from 'react';
import Navbar from "@/components/_App/Navbar";
import Footer from "@/components/_App/Footer";
import PageBanner from '@/components/Common/PageBanner';
import Link from 'next/link';
import { useRouter } from 'next/router';


const SignUp = () => {
    const router = useRouter();

    const [formData, setFormData] = useState({
        email: '',
        password: '',
        confirmPassword: ''
    });

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.id]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        
        try {
            const response = await fetch('http://localhost:5000/api/signup', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            });

            if (response.ok) {
                // Signup successful, handle redirection or other actions
                console.log('Signup successful');
                router.push('/login');
            } else {
                // Signup failed, handle error
                console.error('Signup failed');
            }
        } catch (error) {
            console.error('Error:', error);
        }
    };

    return (
        <>
            <Navbar />
            <PageBanner pageTitle="Sign Up" />

            <div className="ptb-80">
                <div className="container">
                    <div className="auth-form">
                        <div className="auth-head">
                            <p>Create a new account</p>
                        </div>

                        <form onSubmit={handleSubmit}>
                            <div className="mb-3">
                                <label htmlFor="email" className="form-label">Email</label>
                                <input type="email" className="form-control" id="email" value={formData.email} onChange={handleChange} />
                            </div>

                            <div className="mb-3">
                                <label htmlFor="password" className="form-label">Password</label>
                                <input type="password" className="form-control" id="password" value={formData.password} onChange={handleChange} />
                            </div>

                            <div className="mb-3">
                                <label htmlFor="confirmPassword" className="form-label">Confirm Password</label>
                                <input type="password" className="form-control" id="confirmPassword" value={formData.confirmPassword} onChange={handleChange} />
                            </div>

                            <button type="submit" className="btn btn-primary">Sign Up</button>
                        </form>

                        <div className="foot">
                            <p>Already have an account yet? <Link href="/login">Login</Link></p>
                        </div>
                    </div>
                </div>
            </div>
            <Footer />
        </>
    );
};

export default SignUp;
