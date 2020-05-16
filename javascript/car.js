var obj = {
    'test-user-user-car': 'lambo',
    'test-user-car2': 'bmw',
    'test-user-shirt': 'test1',
    'test-user-pants': 'test2',
};

var dataList = {
    outfit: [],
    vehicle: [],
};

for (key in obj) {
    if (key.includes('car')) {
        var splitKey = key.split('-');
        var splitOrder = splitKey[2];
        // dataList.vehicle.push({
        //     [splitOrder]: obj[key] });
        // console.log(splitKey)
        console.log(splitOrder);
        console.log(obj[key])
    }
}