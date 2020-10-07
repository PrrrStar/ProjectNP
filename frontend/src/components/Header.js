import React from "react";
import Login from "./Login";
import Logout from "./SignUp";

const Header = () => {
  return (
    <>
      <header id="header">
        <div className="header__logoBox">
          <a href="/">
            <img src="/images/logo-02.jpg" className="header__logo" alt="logo" />
          </a>
        </div>
        <ul className="header__menuBox">
          <li className="header__menu">
            <a href="/mycvs">내편찾기</a>
          </li>
          <li className="header__menu">
            <a>할인행사</a>
          </li>
          <li className="header__menu">
            <a>커뮤니티</a>
          </li>
          <li className="header__menu">
            <a>Brand Story</a>
          </li>
        </ul>
        <nav className="header__auth">
          <Login />
          <Logout />
        </nav>
      </header>
    </>
  );
};

export default Header;
