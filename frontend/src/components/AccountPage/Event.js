import React from "react";
import { getDateAndTime } from '../../utils/formatTime'
import { seats } from '../../utils/commonFunctions'
import './Event.css';

function Event (props) {

  const { event, enroll } = props;

  const dateAndTime = getDateAndTime(event);


  return (
    <>
      <div className="event"
        onClick={ () => {
          enroll.toggleEnrollPopup()
          enroll.handleEventClick(event, seats(event), dateAndTime);
        }}
      >
        <div className="event__date">
          <p className="event__day">{dateAndTime.dayNumber}</p>
          <p className="event__month">{dateAndTime.monthName}</p>
        </div>
        <p className="event__about">{event.title}</p>
      </div>
    </>
  )
}

export default Event;