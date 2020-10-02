import React from 'react';
import Header from './Header';
import Banner from './Banner';
import Category from './Category';
import '../css/reset.css';
import '../css/base.css';

const App = () => {
  return (
    <>
      <Header />
      <Banner />
      <Category />
    </>
  );
};

export default App;