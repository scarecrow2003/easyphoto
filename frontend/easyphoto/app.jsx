import React from 'react';
import ReactDOM from 'react-dom';
import {Router, IndexRoute, Route, browserHistory} from 'react-router';
import Home from 'app/components/Home.jsx';
import Dashboard from 'dashboard/components/Dashboard';

const routeConfig = [
  {path: 'app', component: Home,
    childRoutes: [
      {path: 'dashboard', component: Dashboard}
    ]
  }
];

ReactDOM.render(<Router history={browserHistory} routes={routeConfig} />, document.getElementById('content'));

