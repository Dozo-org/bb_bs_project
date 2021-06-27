
  export default function formatTime(timeInUtc) {
    const arrTimeUtc = timeInUtc.split("T");
    const arrDate = arrTimeUtc[0].split("-");
    const arrClock = arrTimeUtc[0].split("-");
    return {
      year: arrDate[0],
      month: arrDate[1],
      day: arrDate[2],
      hour: arrClock[0],
      minute: arrClock[1],
    };
  }