function modifyArray(nums) {
    let numbers = [];
    for (var i = 0; i < nums.length; i++) {
        if ((i+1) % 2 !== 0) {
            numbers.push(nums[i]*3);
        } else {
            numbers.push(nums[i]*2);
        }
    }
    return numbers;
}

angkaDeret = [14, 25, 36, 47, 58, 69, 70, 81, 92];
console.log(modifyArray(angkaDeret));