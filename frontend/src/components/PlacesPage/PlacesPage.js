import React, { useEffect } from "react";
import CurrentUserContext from "../../context/CurrentUserContext";
import api from "../../utils/api";

function PlacesPage({ toggleCityPopup, isLoggedIn, city = 1 }) {
  const userData = React.useContext(CurrentUserContext);
  const [cityId, setCityId] = React.useState(0);
  useEffect(() => {
    if (!isLoggedIn) {
      toggleCityPopup();
      setCityId(userData.city || city);
    }
  }, []);

  useEffect(() => {
    api.getPlaces().then((res) => console.log(res));
  }, [cityId]);

  return <>Ура</>;
}
export default PlacesPage;
