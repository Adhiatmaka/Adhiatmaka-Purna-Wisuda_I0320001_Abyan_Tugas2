#Persegi Panjang
print("==== Menghitung Luas dari Persegi Panjang ====")
Panjang = float(input("Panjang dari persegi panjang:"))
Lebar = float(input("Lebar dari persegi panjang:"))
Luas = (Panjang*Lebar)
print("Luas dari persegi panjang sama dengan",Luas,"satuan")

#Lingkaran
print("==== Menghitung Luas dari Lingkaran ====")
phi = 3.14
Jari_jari = float(input("Jari-jari lingkaran :"))
Luas = Jari_jari*Jari_jari*phi
print("Luas dari lingkaran sama dengan",Luas,"satuan")

#Kubus
print("===== Menghitung dari Luas Kubus =====")
Sisi = float(input("Sisi Kubus :"))
Luas_permukaan = 6*Sisi*Sisi
print("Luas dari permukaan kubus sama dengan",Luas_permukaan,"satuan")

#Konversi Suhu Celcius ke Fahrenheit
print("===== Menghitung Konversi Suhu dari Celcius ke Fahrenheit")
Celcius = float(input("Suhu dalam celcius :"))
Konversi_suhu = (((9/5)*Celcius)+32)
print("Konversi suhu dari celcius ke fahrenheit sama dengan",Konversi_suhu,"°F")

#Konversi Suhu Reamur ke Kelvin
print("Menghitung konversi suhu dari Reamur ke Kelvin")
Reamur = float(input("Suhu dalam reamur :"))
Konversi_suhu = ((5/4)*Reamur)+273
print("Konversi suhu dari reamur ke kelvin sama dengan",Konversi_suhu,"K")