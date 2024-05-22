import React from "react";
import Link from "next/link";

const DiscoverArea = () => {
  return (
    <>
      <div className="discover-area ptb-80">
        <div className="container">
          <div className="row align-items-center">
            <div className="col-lg-6 col-md-12">
              <div className="discover-image">
                <img
                  src="/images/homeimg3.jpeg"
                  alt="image"
                />
                <img
                  src="/images/homeimg4.jpeg"
                  alt="image"
                  style={{ height: '270px', width: '350px' }}
                />
              </div>
            </div>

            <div className="col-lg-6 col-md-12">
              <div className="discover-content">
                <h2>Engaging New Audiences through Smart Approach</h2>
                <p>
                Maximize your profits by leveraging our website's accurate price predictions. With real-time market data and advanced tools at your fingertips, making informed decisions has never been easier. Join us now and reap the benefits of smarter farming strategies. Your success starts here!"
                </p>

                <Link href="#" className="btn btn-primary">
                  Discover More
                </Link>
              </div>
            </div>
          </div>
        </div>

        <div className="analytics-shape1">
          <img
            src="/images/bigdata-analytics/analytics-shape1.png"
            alt="image"
          />
        </div>
      </div>
    </>
  );
};

export default DiscoverArea;
