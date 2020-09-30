import React from 'react';

const Home = () => {
  return (
    <>
      <header id="header">
        <div className="header__logoBox">
          <img src="/images/logo-02.jpg" className="header__logo" onclick="location.href='/'" alt="logo" />
        </div>
        <ul className="header__menuBox">
          <li className="header__menu"><a href="/">내편찾기</a></li>
          <li className="header__menu"><a href="/">할인행사</a></li>
          <li className="header__menu"><a href="/">커뮤니티</a></li>
          <li className="header__menu"><a href="/">Brand Story</a></li>
        </ul>
      </header>
    </>
  );
};

export default Home;