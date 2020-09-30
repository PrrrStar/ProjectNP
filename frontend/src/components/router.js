import React from "react";
import { HashRouter as Router, Route, Switch } from "react-router-dom";
import Home from '../routes/Home';

const AppRouter = () => {
    return (
        <Router>
            <Switch>
                <Route path="/">
                    <Home />
                </Route>
            </Switch>
        </Router>
    );
};

export default AppRouter;
