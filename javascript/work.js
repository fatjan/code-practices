const arrA = [
    { nama: 'nama1', alamat: 'alamat1' },
    { nama: 'nama2', alamat: 'alamat2' },
    { nama: 'nama3', alamat: 'alamat3' },
];

const arrB = [
    { tempatlahir: 'tempat1', pekerjaan: 'alamat1' },
    { tempatlahir: 'tempat2', pekerjaan: 'alamat2' },
    { tempatlahir: 'tempat3', pekerjaan: 'alamat3' },
];

for (let i = 0; i < arrB.length; i++) {
    arrA[i].pekerjaan = arrB[i].pekerjaan
}

console.log(arrA)