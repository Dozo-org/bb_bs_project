import { Link } from "react-router-dom";
import "./NotFoundPage.css";
import React from "react";
import Illustration from "../../lotties/Illustration_404.json";
import Animation from "../Animation/Animation.jsx";

function NotFoundPage(props) {

  React.useEffect(() => {
    props.onFooter();
  }, [props])

  return (
    <div className="not-found">
      <Animation
        animationData={Illustration}
        containerClassname="not-found__image"
      />
      <h1 className="not-found__title">404</h1>
      <p className="not-found__info">
        К сожалению, запрашиваемая страница не найдена. Попробуйте перейти на
        главную страницу
      </p>
      <Link to="/main" type="button" className="not-found__button">
        Вернутся на главную
      </Link>
    </div>
  );
}

export default NotFoundPage;