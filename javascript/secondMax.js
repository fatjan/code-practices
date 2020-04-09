function onlyUnique(value, index, self) {
    return self.indexOf(value) === index;
}

const removeFirst = (num, arr) => {
    let newArr = []
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] !== num) {
            newArr.push(arr[i])
        }
    }
    return newArr
}

function getSecondLargest(nums) {
    // Complete the function
    const numsDistinct = nums.filter(onlyUnique)
    const firstMax = Math.max(...numsDistinct);
    const newNums = removeFirst(firstMax, numsDistinct);
    const secondMax = Math.max(...newNums);
    return secondMax;
}

console.log(getSecondLargest([2, 3, 6, 6, 5]));
console.log(getSecondLargest([2, 3, 6, 6, 5, 7, 7, 7, 8, 8, 9, 9, 11, 13, 14, 14, 15]));