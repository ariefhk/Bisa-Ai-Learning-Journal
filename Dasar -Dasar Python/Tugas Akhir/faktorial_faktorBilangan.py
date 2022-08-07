# Faktorial
def faktorial(angka):
    if(angka == 1):
        return 1
    else:
        return angka * faktorial(angka-1)


# Faktor Bilangan
def faktorBilangan(angka):
    hasil = []
    pembagi = 1
    while(pembagi <= angka):
        if(angka % pembagi == 0):
            hasil.append(pembagi)

        pembagi += 1
    return hasil


# Menginputkan Nilai
nilai_faktorial = int(input('Masukan angka untuk mencari Faktorial: '))
nilai_faktorBilangan = int(input('Masukan angka untuk mencari Faktorial Bilangan: '))

# Print Hasil
print(f'faktorial dari {nilai_faktorial} adalah {faktorial(nilai_faktorial)}')
print(f'faktor bilangan dari {nilai_faktorBilangan} adalah {faktorBilangan(nilai_faktorBilangan)}')
