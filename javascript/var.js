var komp = Math.random();
var p = window.prompt("isi 1,2, atau 3 ")
hasil = ''
console.log(komp)
console.log(p);
if (komp < 0.4) {
    komp = "a";

} else if (komp >= 0.4 && komp < 0.6) {
    komp = "b";

} else {
    komp = "c";

    var hasil = " "

    if (komp === p) {
        alert("seri");

    } else if (komp === "a") {
        hasil = (p === "b") ? "kalah" : "menang";

    } else if (komp === "b") {
        hasil = (p === "c") ? "kalah" : "menang";

    } else if (komp === "c") {
        hasil = (p === "a") ? "kalah" : "menang";

    } else {
        hasil = alert("pilih a,b,atau c");
    }
}

alert("kamu memilih" + " " + p + " " + "dan komputer memilih " + komp + " . Kamu " + hasil)