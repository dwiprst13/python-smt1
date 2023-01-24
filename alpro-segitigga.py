
a = int(input("Masukan panjang sisi A segitiga: "))
b = int(input("Masukan panjang sisi B segitiga: "))
c = int(input("Masukan panjang sisi C segitiga: "))

print("="*16)

if a == b and b == c:
    print("Merupakan segitiga sama sisi!!")
elif a == b or b == c or c == a:
    print ("Merupakan segitiga sama kaki!!")
else:
    print("Merupakan segitiga sembarang!!")

print("="*16)