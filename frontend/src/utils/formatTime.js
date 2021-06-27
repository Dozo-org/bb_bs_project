import { format } from 'date-fns'
import { ru } from 'date-fns/locale'
import getUnixTime from "date-fns/getUnixTime";

const dateUnixFormat = (dd) => getUnixTime(new Date(dd));
const date = (dd) => format(new Date(dd),'dd', {locale: ru});
const month = (dd) => format(new Date(dd),'LLLL', {locale: ru});
const time = (dd) => format(new Date(dd),'p', {locale: ru});
const dayOfTheWeek = (dd) => format(new Date(dd), "iiii", { locale: ru });

function getDateAndTime({startAt, endAt}) {

  const monthName = month(startAt);
  const dayName = dayOfTheWeek(startAt);
  const dayNumber = date(startAt);
  const startsAt = time(startAt);
  const endsAt = time(endAt);
  
  return  {
    monthName,
    dayName,
    dayNumber,
    startsAt,
    endsAt
  };
}

  function sortingArrayOrderByDate(arr) {
    return arr.sort(
      (first, last) =>
        dateUnixFormat(first.startAt) - dateUnixFormat(last.startAt)
    );
  }

export {
  date,
  month,
  time,
  dayOfTheWeek,
  dateUnixFormat,
  getDateAndTime,
  sortingArrayOrderByDate,
};


