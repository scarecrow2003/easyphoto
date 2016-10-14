import React from 'react';
import ReactDOM from 'react-dom';
import {Router, IndexRoute, Route, browserHistory} from 'react-router';
import RouterContainer from 'app/RouterContainer';
import Home from 'app/components/Home.jsx';

const routeConfig = [
  {path: 'app', component: Home}
];

ReactDOM.render(<Router history={browserHistory} routes={routeConfig} />, document.getElementById('content'));

