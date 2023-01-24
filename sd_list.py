list1 = [1, -2, -8, 0, 3]
print('Nilai dari list: ', list1)
print("Nilai maksimum dari list:", max(list1))
print(" ")

print('Nilai dari list: ', list1)
print("Nilai minimum dari list:", min(list1))
print(' ')

print("Program memfilter string yang terdiri lebih dari 4 huruf")
list2 = "Pada hari Minggu, Budi dan Ani belajar di rumah Adi, di Desa Konohagure Kecamatan Sukamaju"
print("Original string : ", list2)
list3 = list2.split() 
fword = [i for i in list3 if len(i) > 4]
print('Kata yang lebih dari 4 huruf, antara lain: ', list(fword))
print(' ')

list4 = ['rusa', 'buaya', 'kucing', 'elang', 'bebek']
print('Original List:', list4)
for i in range(len(list4) * 2):
    if i % 2 == 0: 
        list4.insert(i, "a")
print("Memasukan huruf 'a' disetiap isi list: ", list4)
print('')
