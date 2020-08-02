function pingPong(arr, win) {
    let newArr = arr.join(" Pong! ");
    newArr = newArr.split(" ");
    if (win) {
        newArr.push("Pong!")
    }
    return newArr;
}

console.log(pingPong(["Ping!", "Ping!"], false))