function formatDate(userDate) {
    // format from M/D/YYYY to YYYYMMDD
    if (userDate.indexOf('/') === 1) {
        return userDate.slice(5, 9) + userDate.slice(0, 1) + userDate.slice(2, 4);
    } else if (userDate[2] === '/' && userDate.length === 8) {
        return userDate.slice(4, 9) + userDate.slice(0, 2) + userDate[3];
    } else {
        return userDate.slice(6, 10) + userDate.slice(0, 2) + userDate.slice(3, 5);
    }
}

// console.log(formatDate('12/31/2014'));
// console.log(formatDate('1/31/2014'));
console.log(formatDate('12/3/2014'));