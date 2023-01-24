#bilangan ganjil genap
print()
print()
list_angka = (1, 2, 3, 4, 5, 6, 7, 8, 9)
ganjil = 0
genap = 0

for angka in list_angka:
    if angka % 2 == 0:
        genap += 1
    else:
        ganjil += 1

print("list angka: ", list_angka)
print("Jumlah bilangan ganjil:", ganjil)
print("Jumlah bilangan genap:", genap)

# perkalian inputan
print()
print()
angka = int(input("Masukkan angka: "))

for i in range(angka):
    i = i+1
    kali = angka * i
    print(angka, 'x', i, '=', kali)

#fibonacci
print()
print()
a = 1
b = 1
c = 11
d = 0

while d < c:
    print(a)
    ab = a + b
    a = b
    b = ab 
    d += 1

#perkalian 1-10
print()
print()
for j in range(1,11):
    for k in range(1,11):
        print(j*k, end="\t")
    print()



 