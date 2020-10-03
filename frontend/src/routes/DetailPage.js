import React from "react";
import { BrowserRouter, Route, Link, Switch, Router, useParams } from "react-router-dom";

const DetailPage = () => {
  let { slug } = useParams();
  return <div>Now showing post {slug}</div>;
};

export default DetailPage;
