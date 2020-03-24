function decreaseDigit(total) {
    if (total < 10) {
        return total;
    } else {
        const totalString = total.toString();
        var newTotal = 0;
        for (var i = 0; i < totalString.length; i++) {
            newTotal += parseInt(totalString[i]);
        }
        return decreaseDigit(newTotal);
    }
}

function createCheckDigit(membershipId) {
    // Write the code that goes here.
    var total = 0;
    for (var i = 0; i < membershipId.length; i++) {
        total += parseInt(membershipId[i]);
    }
    return decreaseDigit(total);
}

console.log(createCheckDigit('7193235235235235321'));