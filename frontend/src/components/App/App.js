import { useEffect, useState, useCallback, useRef } from "react";
import { Helmet } from "react-helmet-async";
import {
  Route,
  Switch,
  useHistory,
  Redirect,
  useLocation,
} from "react-router-dom";
import Main from "../MainPage/Main/Main";
import Footer from "../Footer/Footer";
import Header from "../Header/Header";
import AuthPopup from "../AuthPopup/AuthPopup";
import AboutUs from "../AboutUsPage/AboutUs";
import api from "../../utils/api";
import Account from "../AccountPage/Account";
import ProtectedRoute from "../ProtectedRoute/ProtectedRoute";
import CurrentUserContext from "../../context/CurrentUserContext";
import Calendar from "../CalendarPage/calendarPage";
import NotFoundPage from "../NotFoundPage/NotFoundPage";
import EnrollPopup from "../EnrollPopup/EnrollPopup";
import ConfirmPopup from "../ConfirmPopup/ConfirmPopup";
import SuccessPopup from "../SuccessPopup/SuccessPopup";
import ErrorPopup from "../ErrorPopup/ErrorPopup";
import CityPopup from "../CityPopup/CityPopup";
import "./App.css";
import { getParticipants } from "../../utils/commonFunctions";
import PlacesPage from "../PlacesPage/PlacesPage";
import QuestionsPage from "../QuestionsPage/QuestionsPage";

function App() {

  const [isLogPopupOpen, setIsLogPopupOpen] = useState(false);
  const [isHeaderMobileOpen, setHeaderMobileOpen] = useState(false);
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [currentUser, setCurrentUser] = useState({});
  const [citiesArray, setCitiesArray] = useState([]);
  const [path, setPath] = useState("");
  const [currentCity, setCurrentCity] = useState(0);
  

  // определение данных пользователя
  function updateUserData(data) {
    setCurrentUser(data);
  }

console.log(currentCity)
  // получает id выбранного города для незареганного
   
  function getCurrentCity (id){
    setCurrentCity(id)
  }

    useEffect(()=> {
      api.getCitiesList().then((res) => {
        setCitiesArray(res.data);
    })
      }, [])


    


  const history = useHistory();
  const loc = useLocation();

  useEffect(() => {
    if (localStorage.getItem("jwt")) {
      api.getUserProfile().then((res) => {
        updateUserData(res.data);
        setIsLoggedIn(true);
        history.push(loc.pathname); 
      });
    }
  }, []);

  

  // при обратном скролле показываем header с display: fixed. При возврщании к началу страницы скрываем класс с фиксом
  const [fixed, setFixed] = useState(false);

  const offsetRef = useRef();
  offsetRef.current = 0;
  const offset = 50;

  const checkScroll = useCallback(() => {
    if (
      window.pageYOffset < offsetRef.current &&
      window.pageYOffset > offset &&
      !isLogPopupOpen
    ) {
      setFixed(true);
    } else {
      setFixed(false);
    }
    offsetRef.current = window.pageYOffset;
  }, [isLogPopupOpen]);

  useEffect(() => {
    window.onscroll = () => {
      checkScroll();
    };
  }, [checkScroll]);

  function handleHeaderMobileClick() {
    setHeaderMobileOpen(!isHeaderMobileOpen);
    setFixed(false);
  }

  function handlePopupClose() {
    setIsLogPopupOpen(false);
  }

  function handleLogPopupOpen(data) {
    setIsLogPopupOpen(true);
    setPath(data);
  }

  function handleHeaderCalendarClick() {
    if (isLoggedIn) {
      history.push("/calendar");
    } else {
      handleLogPopupOpen("/calendar");
    }
  }

  function handleProfileLogoClick() {
    if (isLoggedIn) {
      history.push("/account");
    } else {
      handleLogPopupOpen("/account");
    }
  }

  function handleLoginSubmit(data) {
    const { password, username } = data;
  
     api.auth(username, password).then((res) => {
      if (res.data.access) {
        localStorage.setItem("jwt", res.data.refresh);
        handlePopupClose();
      }
    }); 
    api.getUserProfile().then((res)=> {
      updateUserData(res.data);
      setIsLoggedIn(true);
      history.push(path);
    })
  }

  function handleSignOut() {
    localStorage.removeItem("jwt");
    setIsLoggedIn(false);
  }

  // попапы календаря и запись
  const [isEnrollPopupOpen, setIsEnrollPopupOpen] = useState(false);
  const [wasEnrollPopupOpened, setWasEnrollPopupOpened] = useState(false);
  const [isConfirmPopupOpen, setIsConfirmPopupOpen] = useState(false);
  const [isSuccessPopupOpen, setIsSuccessPopupOpen] = useState(false);
  const [isErrorPopupOpen, setIsErrorPopupOpen] = useState(false);
  const [isCityPopupOpen, setIsCityPopupOpen] = useState(false);
  const [clickedEvent, setClickedEvent] = useState(null);

  useEffect(() => {
    setIsErrorPopupOpen(false);
  }, [history]);

  function rememberEnrollPopupOpen(remember) {
    if (remember === false) {
      setWasEnrollPopupOpened(false);
    } else {
      setWasEnrollPopupOpened(true);
    }
  }

  function toggleEnrollPopup() {
    setIsEnrollPopupOpen(!isEnrollPopupOpen);
  }

  function toggleConfirmPopup() {
    setIsConfirmPopupOpen(!isConfirmPopupOpen);
  }

  function toggleSuccessPopup() {
    setIsSuccessPopupOpen(!isSuccessPopupOpen);
  }

  function toggleErrorPopup() {
    setIsErrorPopupOpen(!isErrorPopupOpen);
  }

  function toggleCityPopup() {
    setIsCityPopupOpen(!isCityPopupOpen);
  }

  function handleEnroll(id) {
    api
      .takePartInEvent({ event: id })
      .then((res) => {
        console.log(res);
        toggleSuccessPopup();
        setWasEnrollPopupOpened(false);
      })
      .catch((e) => {
        console.log(e);
        toggleErrorPopup();
      })
      .finally(() => {
        setIsEnrollPopupOpen(false);
        setIsConfirmPopupOpen(false);
      });
  }

  function handleCancell(id) {
    // тут будет апи запрос для отмены записи
    console.log(`отменить мероприятие ${id}`);
    setIsEnrollPopupOpen(false);
  }

  function handleEventClick(event, seats, dateAndTime, participants) {
    setClickedEvent({
      id: event.id,
      booked: event.booked,
      title: event.title,
      participants:
        participants || getParticipants(event.tags.map((obj) => obj.name)),
      contact: event.contact,
      address: event.address,
      description: event.description,
      remainSeats: seats,
      dateAndTime,
    });
  }

  const enrollMechanism = {
    handleEnroll,
    handleCancell,
    toggleEnrollPopup,
    isEnrollPopupOpen,
    rememberEnrollPopupOpen,
    wasEnrollPopupOpened,
    isErrorPopupOpen,
    toggleErrorPopup,
    toggleConfirmPopup,
    isConfirmPopupOpen,
    toggleSuccessPopup,
    isSuccessPopupOpen,
    handleEventClick,
    isCityPopupOpen,
    toggleCityPopup,
  };

  // отображение футера
  const [isNotFoundPage, setIsNotFoundPage] = useState(false);

  function hideFooter() {
    setIsNotFoundPage(true);
  }




  return (
    <>
      <Helmet>
        <title>BBBS</title>
        <link rel="canonical" /* href="https://www.tacobell.com/" */ />
      </Helmet>
      <CurrentUserContext.Provider value={currentUser}>
          <div className="body">
            <div className="page">
             <Header
                isLogged={isLoggedIn}
                onLogoClick={handleProfileLogoClick}
                onCalendarClick={handleHeaderCalendarClick}
                fixed={fixed}
                onMobileHeaderClick={handleHeaderMobileClick}
                isHeaderMobileOpen={isHeaderMobileOpen}
                onChangeCity={toggleCityPopup}
                signOut={handleSignOut}
              />
              <main className="content page__content">
                <Switch>
                  <Route path="/main">
                    <Main isLoggedIn={isLoggedIn} enroll={enrollMechanism} />
                  </Route>
                  <Route path="/about">
                    <AboutUs />
                  </Route>
                  <Route path="/where_to_go">
                    <></>
                  </Route>
                  <ProtectedRoute
                    component={Calendar}
                    path="/calendar"
                    isLoggedIn={isLoggedIn}
                    enroll={enrollMechanism}
                  />
                  <ProtectedRoute
                    component={Account}
                    path="/account"
                    isLoggedIn={isLoggedIn}
                    signOut={handleSignOut}
                    enroll={enrollMechanism}
                    onUserData={updateUserData}
                  />
                  <Route path="/places">
                    <PlacesPage />
                  </Route>
                  <Route path="/questions">
                    <QuestionsPage />
                  </Route>

                  <Route exact path="/">
                    <Redirect to="/main" />
                  </Route>
                  <Route path="*">
                    <NotFoundPage onFooter={hideFooter} />
                  </Route>
                </Switch>
              </main>
              {!isNotFoundPage && <Footer />}
              <AuthPopup
                isOpen={isLogPopupOpen}
                onClose={handlePopupClose}
                onSubmit={handleLoginSubmit}
              />
              <EnrollPopup enroll={enrollMechanism} event={clickedEvent} />
              <ConfirmPopup enroll={enrollMechanism} event={clickedEvent} />
              <SuccessPopup
                enroll={enrollMechanism}
                event={clickedEvent}
                history={history}
              />
              <ErrorPopup enroll={enrollMechanism} />
              <CityPopup
                enroll={enrollMechanism}
                onUserData={updateUserData}
                cities={citiesArray}
                getCurrentCity={getCurrentCity}
              />
            </div>
          </div>
      </CurrentUserContext.Provider>
    </>
  );

  
}

export default App;
