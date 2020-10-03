import React from "react";
import Header from "../components/Header";
import Banner from "../components/Banner";
import Main from "../components/Main";
import "../css/reset.css";
import "../css/base.css";

const MainPage = () => {
  return (
    <>
      <Header />
      <Banner />
      <Main />
    </>
  );
};

export default MainPage;
