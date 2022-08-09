# if
kondisi = True

if kondisi:
    print('Statement akan dieksekusi')
    

# Contoh Kasus
nilai = 80
if nilai >= 80:
    print('Anda lulus')
    
    
# if/else
nilai = 90
if nilai >= 80:
    print('Anda Lulus')
else:
    print('Anda harus ngulang')


# nested if
jumlah_kaki = 4
suara = 'meong'
kategori = 'mamalia'

if jumlah_kaki == 4:
    print('kemungkinan kucing = 25%')
    print('kemungkinan buaya = 25%')
    print('kemungkinan anjing = 25%')
    print('===================')
    if kategori == 'mamalia':
        print('kemungkinan anjing = 75%')
        print('kemungkinan kucing = 75%')
        if suara == 'meong':
            print('kemungkinan kucing = 100%')
else:
    print('bukan hewan')
            
