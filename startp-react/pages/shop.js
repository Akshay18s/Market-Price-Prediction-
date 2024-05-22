import React from 'react';
import Navbar from "@/components/_App/Navbar";
import Footer from "@/components/_App/Footer";
import PageBanner from '@/components/Common/PageBanner';
import ProductCard from '@/components/Shop/ProductCard';
import Prediction from '@/components/Shop/Prediction';
 
const Shop = () => {
    return (
        <>
            <Navbar />
             
             {/* <PageBanner pageTitle="Products" />  */}

            {/* <ProductCard /> */}
           
            < Prediction />
            
            {/* <Footer />  */}
        </>
    )
}

export default Shop;