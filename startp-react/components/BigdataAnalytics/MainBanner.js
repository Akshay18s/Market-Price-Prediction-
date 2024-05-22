import React from "react";
import Link from "next/link";
import * as Icon from "react-feather";

const MainBanner = () => {
  return (
    <>
      <div className="bigdata-analytics-banner">
        <div className="container">
          <div className="bigdata-analytics-content">
            <h1>Crop Price Prediction</h1>
            <p >
              Welcome to CPP[Crop Price Prediction], where insightful data meets precision forecasting, empowering farmers and traders with reliable crop price predictions.
            </p>

            {/* <Link href="/contact" className="btn btn-primary">
              Get Started
            </Link> */}
          </div>
        </div>

        <div className="banner-boxes-area">
          <div className="container">
            <div className="row justify-content-center">
              <div className="col-lg-4 col-sm-6">
                <div className="single-banner-boxes">
                  <div className="icon">
                    <Icon.Server />
                  </div>
                  <h3>Services</h3>
                  <p>
                    We Provide the prediction of prices of various crops depending upon multiple factors including independant factors. 
                  </p>
                </div>
              </div>

              <div className="col-lg-4 col-sm-6">
                <div className="single-banner-boxes">
                  <div className="icon">
                    <Icon.Code />
                  </div>
                  <h3>Latest news and insights</h3>
                  <p>
                  Our predictive models utilize the latest crop data and real-time market news for accurate predictions.
                  </p>
                </div>
              </div>

              <div className="col-lg-4 col-sm-6">
                <div className="single-banner-boxes">
                  <div className="icon">
                    <Icon.Users />
                  </div>
                  <h3>Interactive Solution</h3>
                  <p>
                  Incorporate interactive tools such as price charts and prediction models for user engagement.                 </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default MainBanner;
