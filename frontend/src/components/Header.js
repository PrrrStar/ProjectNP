import React from 'react';

const Header = () => {
  return (
    <>
      <header id="header">
        <div className="header__logoBox">
          <img src="/images/logo-02.jpg" className="header__logo" onclick="location.href='/index'" alt="logo" />
        </div>
        <ul className="header__menuBox">
          <li className="header__menu"><a>내편찾기</a></li>
          <li className="header__menu"><a>할인행사</a></li>
          <li className="header__menu"><a>커뮤니티</a></li>
          <li className="header__menu"><a>Brand Story</a></li>
        </ul>
        <nav className="header__auth">
          <button data-toggle="modal" data-target="#modal-login" id="base__login-btn" className="header__authBtn">
            <img src="/images/person-24px.png" alt="login" />
            <span>Log in</span>
          </button>
          <button data-toggle="modal" data-target="#modal-signup" className="header__authBtn">
            <img src="/images/person-24px.png" alt="signup" />
            <span>Sign up</span>
          </button>
        </nav>
      </header>
    </>
  );
};

export default Header;