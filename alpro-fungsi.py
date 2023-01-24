def sapa_siapa():
    nama = input("Masukkan nama Anda: ")
    print("Hai", nama)

sapa_siapa()

def sapa_siswa():
    prodi = input("Masukkan nama prodi Anda: ")
    kampus = input("Masukkan nama kampus Anda: ")
    
    print("Halo Mahasiswa",prodi, kampus)

sapa_siswa()
sapa_siswa()
sapa_siswa()

# menghitung luas segitiga

def hitung_luas_segitiga():
    alas = float(input("Masukkan alas segitiga: "))
    tinggi = float(input("Masukkan tinggi segitiga: "))
    luas = (alas * tinggi) / 2
    print("Luas segitiga adalah: ",luas)

hitung_luas_segitiga()

# menghitung pangkat

def pangkat(angka, pangkat = 3):
    hasil = 1
    for i in range(0,pangkat):
        hasil = hasil * angka
    return hasil;

print(pangkat(3))
print(pangkat(4,4))
print(pangkat(2,4))

# menjumlahkan deret

def jumlah():
    angka = input("Masukkan angka yang ingin dihitung(gunakan koma untuk memisahkan angka): ")
    angka = angka.split(',')
    angka = [int(i) for i in angka]
    total = 0
    for x in angka:
        total += x
    return total

print("Jumlah: ",jumlah())

# cek ganjil genap
def cek_ganjil_genap():
    angka = int(input("Masukkan angka yang ingin dicek: "))
    if angka%2==0:
        print("genap")
    else:
        print("ganjil")
    return

cek_ganjil_genap()

# rata rata 
def rata_rata():
    a = int(input("Masukkan nilai a: "))
    b = int(input("Masukkan nilai b: "))
    c = int(input("Masukkan nilai c: "))
    return (a+b+c)/3

print("Rata-rata dari nilai yang diinput adalah: ", rata_rata())

# faktorial
def faktorial():
    x = int(input("Masukkan angka yang ingin dihitung faktorialnya: "))
    hasil = 1
    for i in range(2, x + 1):
        hasil *= i
    return hasil

print("Hasil faktorial dari angka yang diinput adalah: ",faktorial())



