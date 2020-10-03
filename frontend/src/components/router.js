import React from "react";
import { BrowserRouter, Route, Link, Switch, Router, useParams } from "react-router-dom";
import MainPage from "../routes/MainPage";
import DetailPage from "../routes/DetailPage";

const AppRouter = () => {
  return (
    <BrowserRouter>
      <Switch>
        <Route exact path="/" component={MainPage} />
        <Route path="/products/:slug" component={DetailPage} />
      </Switch>
    </BrowserRouter>
  );
};

export default AppRouter;
