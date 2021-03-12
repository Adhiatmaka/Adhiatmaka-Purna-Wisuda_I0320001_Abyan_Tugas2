#Biodata utama
Nama = "Adhiatmaka Purna Wisuda"
Nama_panggilan = "Adhi"
NIM = "I0320001"
Tempat_lahir = "Bantul"
Tanggal_lahir = "10 Juni 2001"
Alamat = "Sumber Batikan, Trirenggo, Bantul, Daerah Istimewa Yogyakarta"
SD = "SDN Bantul Timur"
SMP = "SMPN 1 Bantul"
SMA = "SMAN 2 Yogyakarta"
Jurusan = "Teknik Industri"
Universitas = "Universitas Sebelas Maret"
Hobi = "Basket"

#tambahan
Tinggi_badan = 177.5
Berat_badan = 60
Ukuran_sepatu = 43.5
Minuman_favorit = "Es Kelapa Muda"
Makanan_favorit = "Nasi Goreng"
Warna_favorit = "Hitam"
Motto_hidup = "Yen wani ojo wedi wedi, yen wedi ojo wani wani"

#Penghitungan Usia
Tglskrg = 12
Blnskrg = 3
Thnskrg = 2021
Tgllhr = 10
Blnlhr = 6
Thnlhr = 2001
Usia_Hari = (Thnskrg*365 + Blnskrg*30 + Tglskrg) - (Thnlhr*365 + Blnlhr*30 + Tglskrg)
Usia_T = int(Usia_Hari/365)
Usia_B = int((Usia_Hari % 365)/30)
Usia_H = int((Usia_Hari % 365) % 30)

#Hasil
print("===== BIODATA =====")
print("Nama :", Nama)
print("Nama Panggilan :", Nama_panggilan)
print("NIM :", NIM)
print("Tempat Lahir :", Tempat_lahir)
print("Tanggal Lahir :", Tanggal_lahir)
print("Usia :",Usia_T,"tahun",Usia_B,"bulan",Usia_H,"hari")
print("Alamat :", Alamat)
print("Universitas :", Universitas)
print("Program Studi :", Jurusan)
print("Riwayat Pendidikan :")
print("1.", SD)
print("2.", SMP)
print("3.", SMA)
print("Hobi :", Hobi)
print("Tinggi Badan :", Tinggi_badan, "cm")
print("Berat Badan :", Berat_badan, "kg")
print("Ukuran Sepatu :", Ukuran_sepatu)
print("Makanan Favorit :", Makanan_favorit)
print("Minuman Favorit :", Minuman_favorit)
print("Warna Favorit :", Warna_favorit)
print("Motto Hidup :", Motto_hidup)