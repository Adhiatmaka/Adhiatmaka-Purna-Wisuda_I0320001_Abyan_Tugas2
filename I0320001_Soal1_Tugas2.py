print("==== Menghitung Luas dari Persegi Panjang ====")
panjang = float(input("Panjang dari persegi panjang:"))
lebar = float(input("Lebar dari persegi panjang:"))
luas = (panjang*lebar)
print("Luas dari persegi panjang sama dengan",luas,"satuan")

print("==== Menghitung Luas dari Lingkaran ====")
phi = 3.14
jari_jari = float(input("Jari-jari lingkaran :"))
luas = jari_jari*jari_jari*phi
print("Luas dari lingkaran sama dengan",luas,"satuan")

print("===== Menghitung dari Luas Kubus =====")
sisi = float(input("Sisi Kubus :"))
luas_permukaan = 6*sisi*sisi
print("Luas dari permukaan kubus sama dengan",luas_permukaan,"satuan")

print("===== Menghitung Konversi Suhu dari Celcius ke Fahrenheit")
celcius = float(input("Suhu dalam celcius :"))
konversi = (((9/5)*celcius)+32)
print("Konversi suhu dari celcius ke fahrenheit sama dengan",konversi,"derajat")

print("Menghitung konversi suhu dari Reamur ke Kelvin")
reamur = float(input("Suhu dalam reamur :"))
konversi = ((5/4)*reamur)+273
print("Konversi suhu dari reamur ke kelvin sama dengan",konversi,"derajat")