def ubahString(inputString, N, karakterArray, ubahKarakter):
    output = ''
    simpan_number = {} 
    for char in karakterArray:
        simpan_number[char] = 0
    for j in range(len(inputString)):
        huruf = inputString[j]
        for abjad in karakterArray:
            if huruf == abjad:
                # tambahkan kejadian ketika huruf yg sedang dibaca 
                # di inputString = abjad yg sedang dibaca di karakterArray
                simpan_number[abjad] += 1
                # ketika jumlah kejadiannya = N, 
                # ganti huruf dengan ubahKarakter di output
                if simpan_number[abjad] == N:
                    output += ubahKarakter
        if len(inputString[:j+1]) != len(output):
            output += huruf

    return output
