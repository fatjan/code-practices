const arr = [];

function set(data) {
    setTimeout(function() {
        console.log('ini data ', data)
    }, 2000)
}
set(arr);
console.log('ini arr ', arr)

console.log('ini manggil set', set(['ok', 'ya']))