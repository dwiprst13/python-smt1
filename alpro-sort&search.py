# # Program Binary Search
binary_list = int(input('Masukan banyaknya inputan: '))
item_list = []
for x in range(binary_list):
    listt = int(input())
    item_list.append(listt)
item = int(input('Masukan angka yang mau dicari: '))
def binary_search(item_list,item):
	first       = 0
	last = len(item_list)-1
result = binary_search(item_list, item)
indexs = item_list.index(item)
print('Angka', item, ', nilainya', result, 'berada di index ke', indexs)

# Sequential search
binary_seq = int(input('Masukan banyaknya inputan yang akan di sort: '))
seq_s = []
for x in range(binary_seq):
    list_seq = int(input())
    seq_s.append(list_seq)
seqs = int(input('Masukan angka yang mau dicari: '))
def Sequential_Search(seq_s, seqs):
    pos = 0
    found = False
    while pos < len(seq_s) and not found:
        if seq_s[pos] == seqs:
            found = True
        else:
            pos = pos + 1
    return found, pos
print('cari angka ', seqs, ':', Sequential_Search(seq_s,seqs))



# Bublesort
binary_bbl = int(input('Masukan banyaknya inputan yang akan di sort: '))
bbl = []
for x in range(binary_bbl):
    list_bbl = int(input())
    bbl.append(list_bbl)
def bubbleSort(bbl):
    for passnum in range(len(bbl)-1,0,-1):
        for i in range(passnum):
            if bbl[i]<bbl[i+1]:
                temp = bbl[i]
                bbl[i] = bbl[i+1]
                bbl[i+1] = temp

print('Data sebelum di sort', bbl)
bubbleSort(bbl)
print('Data setelah di sort', bbl)


# Selectionsort
binary_slct = int(input('Masukan banyaknya inputan yang akan di sort: '))
slct = []
for x in range(binary_slct):
    list_slct = int(input())
    slct.append(list_slct)
def selectionSort(slct):
   for fillslot in range(len(slct)-1,0,-1):
       maxpos=0
       for location in range(1,fillslot+1):
           if slct[location]>slct[maxpos]:
               maxpos = location

       temp = slct[fillslot]
       slct[fillslot] = slct[maxpos]
       slct[maxpos] = temp

print('data sebelum di sort: ', slct)
selectionSort(slct)
print('data setelah di sort: ', slct)


