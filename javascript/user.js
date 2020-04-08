var user = {
    name: "Virat Kohli",
    address: "New Delhi"
}

function userDetail(name, address) {
    return "Name: " + name + " ,Address: " + address
}

var functionCall1 = userDetail.call(user.name, user.address);
var functionCall2 = userDetail("Virat Kohli", "New Delhi");

console.log("F Call1 ", functionCall1)
console.log("F Call2 ", functionCall2)