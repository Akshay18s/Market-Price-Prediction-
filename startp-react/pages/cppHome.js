import React from 'react';
import NavbarStyleFour from "@/components/_App/NavbarStyleFour";
import MainBanner from '@/components/BigdataAnalytics/MainBanner';
import WhatWeDo from '@/components/BigdataAnalytics/WhatWeDo';
import DiscoverArea from '@/components/BigdataAnalytics/DiscoverArea';
import Services from '@/components/BigdataAnalytics/Services';
import BigdataFunFacts from '@/components/BigdataAnalytics/BigdataFunFacts';


const BigdataAnalytics = () => {
    return (
        <>
            <NavbarStyleFour />

            <MainBanner />

            <WhatWeDo />

            <DiscoverArea />

            <Services />

            <BigdataFunFacts />

           </>
    )
}

export default BigdataAnalytics;