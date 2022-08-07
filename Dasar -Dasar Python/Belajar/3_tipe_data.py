##### Number

# 1.Integer
number = 250
print(number)
print(type(number))

# 2.Float
number = 11.5
print(number)
print(type(number))

# 3.Complex
number = 1 + 4j
print(number)
print(type(number))


##### String
tipe_string_1 = 'String dengan kutip tunggal'
tipe_string_2 = 'String dengan kutip ganda'
tipe_multiline = """
Test ini adalah String 
dengan Tipe Multiline
"""
tipe_string = 'String bersifat Immutable'


print(tipe_string_1)
print(tipe_string_2)
print(tipe_multiline)
print(tipe_string[7])
print(tipe_string[15])
print(tipe_string[7:])
print(tipe_string[:15])
print(tipe_string[7:15])

##### List
var_list = [3,'test',7.5,'b',1,6,4]
print(var_list[2])
print(var_list[-2])
print(var_list[1:4])
print(var_list[:4])
print(var_list[-2:])
print(var_list[1:6:2])

# Menambahkan elemen list
hewan = ['kucing','burung', 'kelinci', 'anjing']
print(hewan)
hewan.append('kuda') #append
print(hewan)

# Menambahkan list pada list
hewan = ['kucing','burung', 'kelinci', 'anjing']
print(hewan)
warna = ['merah', 'kuning', 'hijau']
print(warna)
hewan.extend(warna) #extend
print(hewan)

# Mereplace elemen list
hewan = ['kucing','burung', 'kelinci', 'anjing']
hewan[0] = 'beruang' #target elemen
print(hewan)

# Menghapus elemen list
hewan = ['kucing', 'burung', 'anjing', 'kelinci']
print(hewan)
del hewan[2] # del (berdasarkan indeks)
print(hewan)

hewan = ['kucing', 'burung', 'anjing', 'kelinci']
print(hewan)
hewan.remove('kucing')
print(hewan)

hewan = ['kucing', 'burung', 'anjing', 'kelinci']
print(hewan)

selected_hewan = hewan.pop(0)
print(selected_hewan)

# Operasi pada List
hewan = ['kucing', 'burung', 'anjing', 'kelinci']
angka = [4,2,8,2]

# 1.Menghitung banyaknya elemen
print(len(hewan))

# 2.Mengetahui index ke-berapa
print(hewan.index('kucing'))

# 3.Menghitung banyaknya elemen
print(angka.count(2))

# 4.Mengurutkan list
hewan.sort()
print(hewan)

# 5.Mengurutkan List secara Descending
hewan.sort(reverse=True)
print(hewan)

# 6.Menggabungkan list
print(hewan+angka)

# 7.Mereplikasi menggunakan operator *
print(angka*2)