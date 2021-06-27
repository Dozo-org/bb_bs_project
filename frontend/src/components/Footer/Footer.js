import React from 'react';
import {Link} from 'react-router-dom';
import './Footer.css';

function Footer() {
  return (
    <footer className='footer page__footer'>
      <div className='footer__three-columns'>
        <a href='https://www.nastavniki.org/' className='footer__logo'>Официальный сайт наставников</a>
        <a href="https://www.nastavniki.org/campaign/pomoch-dengami/" type='button' className='footer__donation link'>
            Помочь деньгами
        </a>
        <div className='footer__info'>
          <p className='footer__copyright'>&copy; Старшие Братья Старшие Сестры</p>
          <p className='footer__about'>
            Разработка – студенты{' '}
            <a href='https://praktikum.yandex.ru/' className='footer__link'>
              Яндекс.Практикум
            </a>
          </p>
          <p className='footer__about'>
            Концепция и дизайн –{' '}
            <a href='/#' className='footer__link'>
              krkr.design
            </a>
          </p>
        </div>

        <nav className='navigation navigation_place_footer'>
          <ul className='navigation__links navigation__links_place_footer'>
            <li className='navigation__list navigation__list_place_footer'>
              <Link to="/about" className='navigation__link navigation__link_place_footer'>
                о проекте
              </Link>
            </li>
            <li className='navigation__list navigation__list_place_footer'>
              <Link to='/calendar' className='navigation__link navigation__link_place_footer'>
                календарь
              </Link>
            </li>
            <li className='navigation__list navigation__list_place_footer'>
              <a href='./places.html' className='navigation__link navigation__link_place_footer'>
                куда пойти
              </a>
            </li>
            <li className='navigation__list navigation__list_place_footer'>
              <a href='/#' className='navigation__link navigation__link_place_footer'>
                вопросы
              </a>
            </li>
            <li className='navigation__list navigation__list_place_footer'>
              <a href='/#' className='navigation__link navigation__link_place_footer'>
                читать и смотреть
              </a>
            </li>
            <li className='navigation__list navigation__list_place_footer'>
              <a href='/#' className='navigation__link navigation__link_place_footer'>
                права детей
              </a>
            </li>
            <li className='navigation__list navigation__list_place_footer'>
              <a href='/#' className='navigation__link navigation__link_place_footer'>
                истории
              </a>
            </li>
          </ul>
        </nav>
        <nav className='navigation navigation_place_footer'>
          <ul className='navigation__links navigation__links_place_footer'>
            <li className='navigation__list navigation__list_place_footer'>
              <a
                href='http://facebook.com'
                target='_blank'
                className='navigation__link navigation__link_place_footer'
                rel="noreferrer"
              >
                facebook
              </a>
            </li>
            <li className='navigation__list navigation__list_place_footer'>
              <a
                href='http://vk.com'
                target='_blank'
                className='navigation__link navigation__link_place_footer'
                rel="noreferrer"
              >
                vkontakte
              </a>
            </li>
            <li className='navigation__list navigation__list_place_footer'>
              <a
                href='http://instagram.com'
                target='_blank'
                className='navigation__link navigation__link_place_footer'
                rel="noreferrer"
              >
                instagram
              </a>
            </li>
            <li className='navigation__list navigation__list_place_footer'>
              <a
                href='http://youtube.com'
                target='_blank'
                className='navigation__link navigation__link_place_footer'
                rel="noreferrer"
              >
                youtube
              </a>
            </li>
          </ul>
        </nav>
      </div>
    </footer>
  );
}

export default Footer;
