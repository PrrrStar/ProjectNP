import React from "react";
import { BrowserRouter, Route, Link, Switch } from "react-router-dom";
import Header from "./Header";
import Banner from "./Banner";
import MainPage from "../routes/MainPage";
import DetailPage from "../routes/DetailPage";

const AppRouter = () => {
  return (
    <BrowserRouter>
      <Header />
      <Banner />
      <Switch>
        <Route exact path="/" component={MainPage} />
        <Route path="/products/:slug" component={DetailPage} />
      </Switch>
    </BrowserRouter>
  );
};

export default AppRouter;
