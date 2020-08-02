function humanReadable(seconds,result = "00:00:00") {
    let replace = "";
    if (seconds < 60) {
      replace = seconds < 10 ? "0" + seconds.toString() : seconds.toString();
      result = result.slice(0,6) + replace;
      console.log('result di if seconds ', result)
      return result;
    } else
    if (seconds >= 3600) {
      let hour = Math.floor(seconds/3600);
      seconds %= 60;
      replace = hour < 10 ? "0" + hour.toString() : hour.toString();
      result = replace + result.slice(2,8);
      console.log('result di if hours ', result)
    } else
    if (seconds >= 60) {
      let minute = Math.floor(seconds/60);
      seconds %= 60;
      replace = minute < 10 ? "0" + minute.toString() : minute.toString();
      result = result.slice(0,3) + replace + result.slice(5,8);
      console.log('result di if minutes ', result)
    } 
    humanReadable(seconds, result)
  }

console.log(humanReadable(0));
console.log(humanReadable(5));
console.log(humanReadable(60));
console.log(humanReadable(70));
// console.log(humanReadable(90));
// console.log(humanReadable(3679));
// console.log(humanReadable(7290));

