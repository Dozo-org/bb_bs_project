import React from "react";
import { Link } from "react-router-dom";
import "./Header.css";
import CurrentUserContext from "../../context/CurrentUserContext";

function Header(props) {
  const userData = React.useContext(CurrentUserContext);

    return (
      <>
        <header
          className={
            props.fixed
              ? "header page__header header_type_position-fixed"
              : "header page__header"
          }
        >
          <Link to="/main" className="header__logo">
            наставники.про
          </Link>
          <nav className="navigation navigation_place_header">
            <ul className="navigation__links navigation__links_place_header">
              <li className="navigation__list">
                <Link
                  to="/calendar"
                  onClick={props.onCalendarClick}
                  className="navigation__link navigation__link_place_header"
                >
                  календарь
                </Link>
              </li>
              <li className="navigation__list">
                <Link
                  to="/places"
                  className="navigation__link navigation__link_place_header"
                >
                  куда пойти
                </Link>
              </li>
              <li className="navigation__list">
                <Link
                  to="/questions"
                  className="navigation__link navigation__link_place_header"
                >
                  вопросы
                </Link>
              </li>
              <li className="navigation__list">
                <Link
                  to="#"
                  className="navigation__link navigation__link_place_header"
                >
                  читать и смотреть
                </Link>
              </li>
              <li className="navigation__list">
                <Link
                  to="#"
                  className="navigation__link navigation__link_place_header"
                >
                  права детей
                </Link>
              </li>
              <li className="navigation__list">
                <Link
                  to="#"
                  className="navigation__link navigation__link_place_header"
                >
                  истории
                </Link>
              </li>
            </ul>
          </nav>
          <form
            action="#"
            name="searcg"
            className="header__form-search display-none"
            method="POST"
          >
            <label className="header__field">
              <input
                id="search-input"
                required
                name="search"
                minLength={2}
                maxLength={40}
                className="header__input"
                type="text"
              />
              <span className="header__input-error" />
            </label>
            <div className="header__answer">
              <p className="header__title">Причины подростковой агрессии</p>
              <p className="header__category">статьи</p>
            </div>
            <div className="header__answer">
              <p className="header__title">Агрессивное поведение детей-сирот</p>
              <p className="header__category">видео</p>
            </div>
            <div className="header__answer">
              <p className="header__title">
                Что делать если ваш младший агрессивно себя ведет, решил закрыть
                пару?
              </p>
              <p className="header__category">книги</p>
            </div>
          </form>
          <button type="button" className="header__search" />
          <div className="header__divisor" />
          <button
            type="button"
            onClick={props.onLogoClick}
            className={
              props.isLogged
                ? "header__account header__account_authorized"
                : "header__account"
            }
          />
          <button
            type="button"
            className="header__menu"
            onClick={props.onMobileHeaderClick}
          />
        </header>

        <div
          className={
            props.isHeaderMobileOpen ? "popup-menu visible-block" : "popup-menu"
          }
        >
          <div className="popup-menu__header">
            <button type="button" className="popup-menu__search" />
            <button
              type="button"
              onClick={props.onLogoClick}
              className="popup-menu__account"
            />
            <Link to="#" className="popup-menu__logo">
              наставники.про
            </Link>
            <button
              type="button"
              aria-label="close popup"
              className="popup-menu__close"
              onClick={props.onMobileHeaderClick}
            />
          </div>
          <nav className="popup-menu__navigation">
            <ul className="popup-menu__links">
              <li className="popup-menu__list">
                <Link to="/about" className="popup-menu__link">
                  о проекте
                </Link>
              </li>
              <li className="popup-menu__list">
                <Link
                  to="/calendar"
                  className="popup-menu__link"
                  onClick={props.onCalendarClick}
                >
                  календарь
                </Link>
              </li>
              <li className="popup-menu__list">
                <Link to="#" className="popup-menu__link">
                  куда пойти
                </Link>
              </li>
              <li className="popup-menu__list">
                <Link to="/questions" className="popup-menu__link">
                  вопросы
                </Link>
              </li>
              <li className="popup-menu__list">
                <Link to="#" className="popup-menu__link">
                  читать и смотреть
                </Link>
              </li>
              <li className="popup-menu__list">
                <Link to="#" className="popup-menu__link">
                  права детей
                </Link>
              </li>
              <li className="popup-menu__list">
                <Link to="#" className="popup-menu__link">
                  истории
                </Link>
              </li>
            </ul>
            <ul className="popup-menu__links">
              <li className="popup-menu__list">
                <a href="http://facebook.com" className="popup-menu__link">
                  facebook
                </a>
              </li>
              <li className="popup-menu__list">
                <a href="http://vk.com" className="popup-menu__link">
                  vkontakte
                </a>
              </li>
              <li className="popup-menu__list">
                <a href="http://instagram.com" className="popup-menu__link">
                  instagram
                </a>
              </li>
              <li className="popup-menu__list">
                <a href="http://youtube.com" className="popup-menu__link">
                  youtube
                </a>
              </li>
            </ul>
          </nav>
          {props.isLogged &&  (
            <div className="popup-menu__footer">
              <p className="popup_menu__city">{userData.city.name}.</p>
              <button
                type="button"
                className="popup-menu__change-city"
                onClick={() => {
                  props.onMobileHeaderClick();
                  props.onChangeCity();
                }}
              >
                Изменить город
              </button>
              <button
                type="button"
                className="popup-menu__exit"
                onClick={() => {
                  props.onMobileHeaderClick();
                  props.signOut();
                }}
              >
                Выйти
              </button>
            </div>
          )}
        </div>
      </>
    );
  }

export default Header;
