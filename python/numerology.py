# program ini untuk membantu menghitung angka sesuai Numerology rules yang ada di
# https://ramal.id/ramalan-nasib-masa-depan/#Ramalan_Nasib_Masa_Depan_Berdasarkan_Nama_dan_Tanggal_Lahir


tanggal = 'tanggal'
while tanggal.isnumeric() == False:
    tanggal = input('Masukan tanggal kelahiran Anda : ')

bulan = 'bulan'
while bulan.isnumeric() == False:
    bulan = input('Masukan bulan kelahiran Anda dalam bentuk angka : ')

tahun = 'tahun'
while tahun.isnumeric() == False and len(tahun) != 4:
    tahun = input('Masukan tahun kelahiran Anda : ')

print("Anda lahir pada ", tanggal, bulan, tahun)

while len(tanggal) > 1:
    total_1 = 0
    for char in tanggal:
        total_1 += int(char)
    tanggal = str(total_1)
else:
    total_1 = int(tanggal)

while len(bulan) > 1:
    total_2 = 0
    for num in bulan:
        total_2 += int(num)
    bulan = str(total_2)
else:
    total_2 = int(bulan)

while len(tahun) > 1:
    total_3 = 0
    for year in tahun:
        total_3 += int(year)
    tahun = str(total_3)

total =  total_1 + total_2 + total_3
total_akhir = str(total)
while len(total_akhir) > 1:
    total = 0
    for angka in total_akhir:
        total += int(angka)
    total_akhir = str(total)

print('Angka Numerologi Anda adalah ', total)
