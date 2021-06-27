import React from "react";
import "./SuccessPopup.css";
// eslint-disable-next-line import/extensions,import/no-unresolved
import Animation from "../Animation/Animation";
import success from "../../lotties/success.json";

function SuccessPopup(props) {
  const { enroll, history, event } = props;

  function goToCalendar() {
    history.push("/calendar");
    enroll.toggleSuccessPopup();
  }

  return (
    <div
      className={
        enroll.isSuccessPopupOpen
          ? "visible-block popup popup-calendar popup-calendar_type_done"
          : "popup popup-calendar popup-calendar_type_done"
      }
    >
      {event && (
        <div className="popup-calendar__content">
          <button
            type="button"
            aria-label="close popup"
            className="popup__close popup__close_type_calendar"
            onClick={() => enroll.toggleSuccessPopup()}
          />
          <Animation
            animationData={success}
            containerClassname="popup-calendar__img"
          />
          <p className="list__done">
            Вы записаны на мероприятие
            <br />
            {event.title}
          </p>
          <p className="list__done">
            Если у вас не получится прийти — отмените, пожалуйста, запись.
          </p>
          <div className="list__buttons">
            <button
              type="submit"
              className="list__submit list__submit_return"
              onClick={() => goToCalendar()}
            >
              Вернуться к календарю
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

export default SuccessPopup;
