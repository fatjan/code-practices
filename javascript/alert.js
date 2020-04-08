function test1() {
    var a = 1;
    console.log(a);
    if (true) {
        var a;
        console.log(a);
        a = 2;
    }
    console.log(a);
}
test1();