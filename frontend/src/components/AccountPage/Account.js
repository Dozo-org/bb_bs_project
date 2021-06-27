import React from "react";
import Event from "./Event";
import CurrentUserContext from "../../context/CurrentUserContext";
import api from "../../utils/api";
import { sortingArrayOrderByDate } from "../../utils/formatTime";
import Loader from '../Loader/Loader';
import './Account.css';


function Account(props) {
  const userData = React.useContext(CurrentUserContext);
  const [events, setEvents] = React.useState([]);
  const [isContentReady, setIsContentReady] = React.useState(false)

  React.useEffect(() => {
    api.getEvents().then((res) => {
      setEvents(res.data);
      setIsContentReady(true);
    });
  }, [])


if(isContentReady) {
  return (
    <>
      <section className="account">
        <div className="account__buttons">
          <button type="button" className="account__button" onClick={() => props.enroll.toggleCityPopup()}>
            {userData.city.name}. Изменить ваш город
          </button>
          <button
            type="button"
            onClick={props.signOut}
            className="account__button"
          >
            Выйти
          </button>
        </div>
        <p className="account__events-text">
          {events.length !== 0
            ? "Вы записаны на мероприятия:"
            : "У вас нет записи на мероприятие"}
        </p>
        <div className="account__events">
          <div className="account__scroll">
            {events.length !== 0 &&
              sortingArrayOrderByDate(events).map(
                (event) =>
                  event.booked && (
                    <Event key={event.id} event={event} enroll={props.enroll} />
                  )
              )}
          </div>
        </div>
      </section>
      {/* <CityPopup 
        enroll={props.enroll}
        onUserData={props.onUserData}
        cities={props.cities}
      /> */}
    </>
  );
}  return <Loader />
  
}

export default Account;
