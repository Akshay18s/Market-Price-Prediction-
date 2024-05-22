import React from 'react';
import Navbar from "@/components/_App/Navbar";
import MainBanner from '@/components/BigdataAnalytics/MainBanner';
import WhatWeDo from '@/components/BigdataAnalytics/WhatWeDo';
import DiscoverArea from '@/components/BigdataAnalytics/DiscoverArea';
import Services from '@/components/BigdataAnalytics/Services';
import TeamStyleTwo from '@/components/Common/TeamStyleTwo';
import BigdataFunFacts from '@/components/BigdataAnalytics/BigdataFunFacts';
import Feedback from '@/components/BigdataAnalytics/Feedback';
import IndustriesWeServe from '@/components/BigdataAnalytics/IndustriesWeServe';
import BlogPost from '@/components/BigdataAnalytics/BlogPost';
import Footer from "@/components/_App/Footer";

const Index = () => {
    return (
        <>
            <Navbar />

            <MainBanner />

            <WhatWeDo />

            <DiscoverArea />

            <Services />

            <TeamStyleTwo />

            <BigdataFunFacts />

            <Feedback />

            <IndustriesWeServe />

            <BlogPost />

            
            <Footer />
        </>
    )
}

export default Index;