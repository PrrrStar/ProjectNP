import React from 'react';

const Header = () => {
  return (
    <>
      <header id="header">
        <div className="header__logoBox">
          <img src="/images/logo-02.jpg" className="header__logo" onclick="location.href='/index'" />
        </div>
        <ul className="header__menuBox">
          <li className="header__menu"><a href="{% url 'mymap' %}">내편찾기</a></li>
          <li className="header__menu"><a href="#">할인행사</a></li>
          <li className="header__menu"><a href="{% url 'post_list' %}">커뮤니티</a></li>
          <li className="header__menu"><a href="#">Brand Story</a></li>
        </ul>
        <nav className="header__auth">
          <button data-toggle="modal" data-target="#modal-login" id="base__login-btn" className="header__authBtn">
            <img src="/images/person-24px.png" />
            <span>Log in</span>
          </button>
          <button data-toggle="modal" data-target="#modal-signup" className="header__authBtn">
            <img src="/images/person-24px.png" />
            <span>Sign up</span>
          </button>
        </nav>
      </header>
    </>
  );
};

export default Header;