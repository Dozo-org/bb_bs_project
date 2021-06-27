// участники мероприятия
function addPlus(array, obj) {
  if (array.length > 1) {
    if (array.indexOf(obj) !== array.length - 1) {
      return `${obj} + `
    }  
  } return obj
}

function getParticipants(array) {
  return array.map((obj) => (addPlus(array, obj))).join('');
}

// количество мест
function checkNum(num) {
  switch (true) {
    case num === 1:
      return "место";
    case num >= 5:
      return "мест";
    default:
      return "места";
  }
}

function seats(event) {
  if (event.remainSeats && event.remainSeats > 0) {
    return `Осталось ${event.remainSeats} ${checkNum(event.remainSeats)}`;
  }

  const remainSeats = event.seats - event.takenSeats;

  if (remainSeats > 0) {
    return `Осталось ${remainSeats} ${checkNum(remainSeats)}`;
  }

  return 'Запись закрыта';
}  

export  { getParticipants, seats } ;