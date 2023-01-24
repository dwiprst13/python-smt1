#penjummlahan
buku = 12000
pensil = 9000
total_harga = buku + pensil
print(total_harga)

#pengurangan
utang = 5000
dibayar = 2000
sisa_utang = utang - dibayar
print(sisa_utang )

#perkalian
alas = 4
tinggi = 5
luas = alas * tinggi
print(luas)

#pembagian
angka1 = 21
angka2 = 3
hasil_pembagian = angka1 / angka2
print(hasil_pembagian)

#pangkat
a = 2
print(a**2)

#sisa bagi / modulus 
b = 10
print(b%3)

#luas persegi
sisi = int(input("Masukkan sisi persegi: "))
luas_persegi = sisi * sisi
print ("luas persegi adalah: ", luas_persegi)

#luas persegi panjang
panjang = int(input("Masukkan panjang: "))
lebar = int(input("Masukkan lebar: "))
luas_persegi_panjang = panjang * lebar
print ("Luas persegi panjang adalah: ",luas_persegi_panjang)

#Menghitung Luas segitiga
alas = int(input("Masukkan alas :"))
tinggi = int(input("Masukkan tinggi: "))
luas_segitiga = 0.5 * alas * tinggi
print ("Luas segitiga adalah: ", luas_segitiga)

#luas lingkaran
r = float(input("masukkan jari jari: "))
luas_lingkaran = 3.14 * r*r
print ("luas lingkaran adalah : ",luas_lingkaran)

#luas trapesium
sisi_atas = int(input("Masukkan sisi atas :"))
sisi_bawah = int(input("Masukkan sisi bawah :"))
tinggi_tr = int(input("Masukkan tinggi trapesium :"))
luas_trapesium = 0.5 * (sisi_atas + sisi_bawah) * tinggi_tr
print ("Luas trapesium adalah: ", luas_trapesium) 
