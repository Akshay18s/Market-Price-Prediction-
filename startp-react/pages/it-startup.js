import React from 'react';
import Navbar from "@/components/_App/Navbar";
import MainBanner from "@/components/cppHome/MainBanner";
import Features from "@/components/ cppHome/Features";
import OurFeatures from "@/components/cppHome/OurFeatures";
import ServicesArea from "@/components/cppHome/ServicesArea";
import Team from "@/components/Common/Team";
import FunFactsArea from "@/components/Common/FunFactsArea";
import RecentWorks from "@/components/Common/RecentWorks";
import PricingStyleOne from "@/components/PricingPlans/PricingStyleOne";
import Feedback from "@/components/Common/Feedback";
import Partner from "@/components/Common/Partner";
import BlogPost from "@/components/Common/BlogPost";
import Footer from "@/components/_App/Footer";

const ITStartup = () => {
    return (
        <>
            <Navbar />

            <MainBanner />

            <Features />

            <ServicesArea />

            <OurFeatures />

            <Team />

            <FunFactsArea />

            <RecentWorks />

            <PricingStyleOne />

            <Feedback />

            <Partner />

            <BlogPost />
            
            <Footer />
        </>
    )
}

export default ITStartup;