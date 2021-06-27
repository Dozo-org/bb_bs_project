import React from "react";
import './EnrollPopup.css';


function EnrollPopup(props) {

  const { enroll, event } = props;
  const { id, dateAndTime } = event || {};

  return (
    <div className={ enroll.isEnrollPopupOpen ? "visible-block popup popup-calendar popup-calendar_type_event" : "popup popup-calendar popup-calendar_type_event" }>
      { event &&
        <div className="popup-calendar__content">
          <button 
            type="button" 
            aria-label="close popup" 
            className="popup__close popup__close_type_calendar" 
            onClick={() => enroll.toggleEnrollPopup()}
          />
          <div className="list__header">
            <p className="list__caption">
              {event.participants}
            </p>
            <p className="list__date">{`${dateAndTime.monthName} / ${dateAndTime.dayName}`}</p>
          </div>
          <div className="list__theme">
            <h2 className="list__title">{event.title}</h2>
            <p className="list__number">{dateAndTime.dayNumber}</p>
          </div>
          <div className="list__contacts">
            <p className="list__contact">{`${dateAndTime.startsAt}-${dateAndTime.endsAt}`}</p>
            <p className="list__contact list__contact_center">{event.address}
            </p>
            <p className="list__contact">{event.contact}</p>
          </div>
          <p className="list__event">{event.description}</p>
          <div className="list__footer">
            <button 
              type="submit" 
              className={ event.booked ? "list__submit_is-registered list__submit list__submit_type_register-popup" : "list__submit list__submit_type_register-popup" }
              onClick={ !event.booked ? () => enroll.handleEnroll(id) : () => enroll.handleCancell(id) }
            >
              { !event.booked ? "Записаться" : "Отменить запись" } 
            </button>
            <p className="list__place-number">{event.remainSeats}</p>
          </div>
      </div>  
      }
    </div>
  );
}

export default EnrollPopup;
