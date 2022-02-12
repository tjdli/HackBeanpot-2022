import logo from './logo.svg';
import React, { Suspense, lazy } from 'react';
import './App.css';
import Button from '@material-ui/core/Button';
import { BrowserRouter, Switch, Route } from 'react-router-dom';

const Index = lazy(() => import('./Pages/Index'));

function App() {
  <Switch>
    <Route path="/" component={Index}/>
  </Switch>
};

export default App;
