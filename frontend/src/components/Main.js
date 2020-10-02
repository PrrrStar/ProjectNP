import React from "react";
import Category from "./Category";
import "../css/index.css";
import MainIndex from "./MainIndex";

const Main = () => {
  return (
    <div className="main">
      <Category />
      <MainIndex />
    </div>
  );
};

export default Main;
