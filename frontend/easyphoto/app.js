import React from 'react';
import ReactDOM from 'react-dom';
import {createStore, combineReducers} from 'redux';
import {Provider} from 'react-redux';
import {Router, IndexRoute, Route, browserHistory} from 'react-router';
import {syncHistoryWithStore, routerReducer} from 'react-router-redux';
import jobReducer from 'job/reducers/jobReducer';
import Home from 'app/components/Home';
import Dashboard from 'dashboard/components/Dashboard';
import Job from 'job/components/Job';

const routeConfig = [
  {path: 'app', component: Home,
    childRoutes: [
      {path: 'dashboard', component: Dashboard},
      {path: 'job', component: Job}
    ]
  }
];

const store = createStore(
    combineReducers({
        jobReducer,
        routing: routerReducer
    })
);

ReactDOM.render(
    <Provider store={store}>
        <Router history={syncHistoryWithStore(browserHistory, store)} routes={routeConfig}/>
    </Provider>,
    document.getElementById('content')
);