def ubahString(inputString, N, karakterArray, ubahKarakter):
    # simpan_number merupakan dictionary untuk menyimpan 
    # banyaknya kejadian karakterArray di inputString
    simpan_number = {} 
    for char in karakterArray:
        simpan_number[char] = 0
    
    output = ''

    for j in range(len(inputString)):
        huruf = inputString[j]
        for abjad in karakterArray:
            if huruf == abjad:
                # tambahkan kejadian ketika huruf yg sedang 
                # dibaca di inputString = abjad yg sedang dibaca di karakterArray
                simpan_number[abjad] += 1
                # ketika jumlah kejadiannya = N, 
                # ganti huruf dengan ubahKarakter di output
                if simpan_number[abjad] == N:
                    output += ubahKarakter
        # masukkan huruf ke dalam output jika karakter tidak diganti 
        # huruf tidak diganti dengan ubahKarakter maka panjang string inputString dari awal sampai index j
        # tidak akan sama dengan panjang string output sebelum ditambahkan huruf
        if len(inputString[:j+1]) != len(output):
            output += huruf

    return output

# print(ubahString("kotakode", 2 , ['k','o'], "*"))

# print(ubahString("kotakode adalah sebuah situs untuk programmer", 3 , ['k','a','o'], "*"))

# print(ubahString("mari kita belajar python", 1 , ['a','r'], "*"))

# time complexity: O(n^2) dimana n adalah jumlah panjang string dari inputString