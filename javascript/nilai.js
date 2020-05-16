const siswa = {
    nilai: [56, 78, 93, 100],
    dataNilai: function() {
        let x = this.nilai.filter((item) => {
            if (item % 2 !== 0) {
                console.log(item)
                return item
            }
        })
    }
}

// siswa.dataNilai()
siswa.dataNilai.x;