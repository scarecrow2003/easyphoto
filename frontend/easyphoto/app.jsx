import React from 'react';
import ReactDOM from 'react-dom';
import {Router, IndexRoute, Route, browserHistory} from 'react-router';
import Home from 'app/components/Home.jsx';
import Login from 'login/components/Login';
import Signup from 'login/components/Signup';

const routeConfig = [
  {path: 'app', component: Home},
  {path: 'onboarding/login', component: Login},
  {path: 'onboarding/signup', component: Signup}
];

ReactDOM.render(<Router history={browserHistory} routes={routeConfig} />, document.getElementById('content'));

