let data = [
    { a: 1, b: 200 },
    { a: 2, b: 400 },
    { a: 3, b: 500 },
    { a: 4, b: 700 }
  ];
let data2 = data.shift();
console.log('data2 ', data2)
let data3 = data2.b;
console.log("data2.b: " + data2.b);
console.log("data3: " + data3);





// keep this 

// calculate failure rates for each stage
    // Object.keys(stages).forEach(level => {
    //     failureRates[level] = stages[level] / remainder
    //     remainder -= stages[level]
    // });

// find the order of failure rates from biggest to lowest
// var order = {};
// var maxNow = '';
// var index = '';
// var answer = [];
// console.log(failureRates)
// // Object.keys(failureRates).forEach(rate => {
// //     maxNow = listOfFailureRates.length > 0 ? 
// //         Math.max.apply(null, listOfFailureRates) : 0;
// //     order[rate] = maxNow
// //     index = listOfFailureRates.indexOf(order[rate]);
// //     listOfFailureRates.splice(index, 1);
// // });

// Objects.keys(failureRates).forEach(rate => {
//         maxNow = listOfFailureRates.length > 0 ?
//                     Math.max.apply(null, listOfFailureRates) : 0; 
//     }
// );

// // console.log(order);
// Object.keys(order).forEach(orderKey => {
//         Object.keys(failureRates).forEach(rate => {
//                 // console.log(rate);
//                 // console.log(failureRates[rate]);
//                 if (order[orderKey] === failureRates[rate] & !(rate in answer)) {
//                     answer.push(failureRates[rate]);
//                 };
//             }
//         );
//     }
// );
// revFailureRates = {};
// // reverse the key value pair of failureRates
// Object.keys(failureRates).forEach(rate => {
//         key = failureRates[rate];
//         if (!(key in failureRates)) {
//             revFailureRates[key] = [rate];
//             console.log(rate)
//         } else {
//             console.log('else ', rate)
//             revFailureRates[key].push(rate);
//         }
//         console.log(revFailureRates)
//     }
// );
// console.log(revFailureRates)
// return answer;