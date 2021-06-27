import React from "react";
import './ErrorPopup.css';

function ErrorPopup(props) {
  const { isErrorPopupOpen, wasEnrollPopupOpened, toggleErrorPopup, toggleEnrollPopup } = props.enroll;

  function handleReturn() {
    toggleErrorPopup();

    if (wasEnrollPopupOpened) {
      toggleEnrollPopup();
    } 
  }

  return (
    <div className={ isErrorPopupOpen ? "visible-block popup popup_error" : "popup popup_error" }>
      <div className="popup__container popup__container_type_error">
      <h2 className="list__title list__title_error">
        Что-то пошло не так, попробуйте записаться снова
      </h2>
      <button 
        type="submit" 
        className="list__submit list__submit_type_error"
        onClick={ () => handleReturn() }
      >Вернуться к мероприятию</button>
      </div>
    </div>
  );
}

export default ErrorPopup;
