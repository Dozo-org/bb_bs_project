import React from "react";
import { useForm } from "react-hook-form";
import './AuthPopup.css';

function AuthPopup(props) {

  // валидация формы
  const { register, handleSubmit } = useForm();

  const [red, setRed] = React.useState(false);

  const isEmpty = (obj) => {
    if (Object.keys(obj).length === 0) {
      return true;
    }
    return false;
  }

  const onSubmit = data => {

    props.onSubmit({
      username: data.login,
      password: data.password
    })

    setRed(false);
  };

  const onError = (errs) => {
    if (!isEmpty(errs)) {
      setRed(true);
    }
  };


  return (
    <div className={props.isOpen? 'popup popup-sign-in visible-block' : 'popup popup-sign-in'}>
      <div className="popup__container">
        <button type="button" aria-label="close popup" onClick={props.onClose} className="popup__close" />
        <h2 className="popup__title">Вход</h2>
        <p className="popup__message">Вход в личный кабинет доступен наставникам программы «Старшие Братья Старшие
            Сёстры».</p>
        <p className="popup__message">Пожалуйста, введите логин и пароль из письма. Если вам не приходило письмо,
            свяжитесь с вашим куратором.</p>
        <form action="#" name="sign-in" className="popup__form" onSubmit={handleSubmit(onSubmit, onError)} noValidate>
          <label className="popup__field">
            <input id="login-input" {...register("login",
              { required: true, minLength: 2, maxLength: 40 })}
              placeholder="Логин"
              className={red ? "popup__input popup__input_error" : "popup__input"} type="text"
              onChange={() => setRed(false)}/>
          </label>
          <label className="popup__field">
            <input id="password-input"
              {...register("password", { required: true, minLength: 8, maxLength: 200 })}
              placeholder="Пароль"
              className={red ? "popup__input popup__input_error" : "popup__input"}
              type="password"
              onChange={() => setRed(false)}  autoComplete="off"/>
          </label>
          <p className="popup__help">Забыли пароль?</p>
          <button
            aria-label="submit form" className="popup__button-submit"
            type="submit">Войти</button>
        </form>
      </div>
    </div>
  )
}

export default AuthPopup;