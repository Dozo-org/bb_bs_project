import instance from "../source/mock";

function checkResponse(res) {
  if (res) {
    return res;
  }
  return Promise.reject(new Error(`Произошла непредвиденная ошибка.`));
}

const headers = {
  headers: {
    "Content-Type": "application/json",
    Authorization: `Bearer ${localStorage.getItem("jwt")}`,
  },
};

function auth(username, password) {
  return instance
    .post(
      "/token",
      { username, password },
      { headers: { "Content-Type": "application/json" } }
    )
    .then((res) => checkResponse(res));
}

function getCitiesList() {
  return instance.get("/cities", headers).then((res) => checkResponse(res));
}

function getUserProfile() {
  return instance.get("/profile", headers).then((res) => checkResponse(res));
}

function getMainPage() {
  return instance.get("/main", headers).then((res) => checkResponse(res));
}

function getEvents() {
  return instance
    .get("/afisha/events", headers)
    .then((res) => checkResponse(res));
}

function takePartInEvent(event) {
  return instance
    .post("/afisha/event-participants/", event, headers)
    .then((res) => checkResponse(res));
}

function changeCity(cityId) {
  return instance
      .patch("/profile", {city: cityId}, headers)
      .then((res) => checkResponse(res))

}

function getPlaces() {
  return instance.get(`places/`);
}

function getQuestions() {
  return instance.get("/questions", headers).then((res) => checkResponse(res));
}

export default {
  auth,
  getCitiesList,
  getUserProfile,
  getMainPage,
  getEvents,
  takePartInEvent,
  changeCity,
  getPlaces,
  getQuestions
};
