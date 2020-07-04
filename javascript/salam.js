function salam(nama){
    return console.log('Halo ' + nama + ', selamat pagi!')
}

salam('Nargo')

// Buatlah fungsi dengan nama tambah, 
// yang menerima parameter bilanganPertama dan bilanganKedua, 
// lalu me-return hasil penjumlahan dari kedua parameter tersebut.

function tambah(bilanganPertama, bilanganKedua){
    return bilanganPertama + bilanganKedua
}

console.log(tambah(2, 9))

const penjelasanArrowFunction = () => {
    const penjelasan = "Arrow function adalah sebuah fungsi yang ... menggunakan notasi arrow atau => ...";
    return console.log(penjelasan);
}

penjelasanArrowFunction()