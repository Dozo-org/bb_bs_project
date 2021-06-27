import './CityPopup.css';
import City from './City/City';
import api from "../../utils/api";


function CityPopup({ enroll, onUserData, cities, getCurrentCity }) {

  const {isCityPopupOpen, toggleCityPopup} = enroll;

  function handleCityChange(id) {
    api.changeCity(id)
      .then((res) => onUserData(res.data))
      getCurrentCity(id)
    toggleCityPopup();
  }



  return (
    <div className={ isCityPopupOpen ? "visible-block popup" : "popup" }>
      <div className="popup__container popup__container_type_city">
        <h2 className="list__title">
          Выберите ваш город
        </h2>
        <ul className="cities-list">
          <div className="cities-list__main">
            {cities.map((city) => (
              city.isPrimary && <City
                key={city.id}
                id={city.id}
                city={city.name}
                handleChange={handleCityChange}
              />
            ))}
          </div>
          {cities.map((city) => (
              !city.isPrimary && <City
                key={city.id}
                id={city.id}
                city={city.name}
                handleChange={handleCityChange}
              />
            ))}
        </ul>
      </div>
    </div>
  )
}

export default CityPopup;