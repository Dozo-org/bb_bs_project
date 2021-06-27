import React from 'react';
import { Link } from 'react-router-dom';
import './Article.css'


function Article() {
  return(
  <Link to="#" className="link">
    <article className="block-guest background-green">
      <div className="block-guest__container-header">
        <div className="block-guest__logo"></div>
      </div>
      <div className="block-guest__container-body">
        <h2 className="block-guest__title">Наставники.про – цифоровая информационная платформа огрганизации «Старшие Братья Старшие Сестры». Созданная для поддержки наставников программы.</h2>
      </div>
    </article>
  </Link>
  )
}

export default Article;

