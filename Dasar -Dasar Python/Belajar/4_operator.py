##### Operator Aritmatika
# +, -, *, /, %, **, //

var_angka1 = 10
var_angka2 = 5

penjumlahan = var_angka1 + var_angka2
pengurangan = var_angka1 - var_angka2
perkalian = var_angka1 * var_angka2
pembagian = var_angka1 / var_angka2
modulus = var_angka1 % var_angka2
pangkat = var_angka1 ** var_angka2
int_pembagian = var_angka1 // var_angka2

print(penjumlahan)
print(pengurangan)
print(perkalian)
print(pembagian)
print(modulus)
print(pangkat)
print(int_pembagian)

##### Operator Perbandingan
# >, <, ==, !=, >=, <=
var_angka1 = 6
var_angka2 = 4

print(f'Lebih dari (>): {var_angka1} > {var_angka2} adalah {var_angka1 >var_angka2} ')
print(f'Kurang dari (<): {var_angka1} < {var_angka2} adalah {var_angka1 < var_angka2} ')
print(f'Sama dengan (==): {var_angka1} == {var_angka2} adalah {var_angka1 == var_angka2} ')
print(f'Tidak sama dengan (!=): {var_angka1} != {var_angka2} adalah {var_angka1 != var_angka2} ')
print(f'Lebih dari sama dengan (>=): {var_angka1} >= {var_angka2} adalah {var_angka1 >= var_angka2} ')
print(f'Kurang dari sama dengan (<=): {var_angka1} <= {var_angka2} adalah {var_angka1 <= var_angka2} ')


##### Operator Perbandingan
# and, or, not

var_angka1 = 8
var_angka2 = 12

print(f'and : {var_angka1} > {var_angka2} and {var_angka1} <= {var_angka2} adalah {(var_angka1 > var_angka2) and (var_angka1 <= var_angka2) }')
print(f'or : {var_angka1} > {var_angka2} and {var_angka1} <= {var_angka2} adalah {(var_angka1 > var_angka2) or (var_angka1 <= var_angka2) }')
print(f'not : not({var_angka1} > {var_angka2}) adalah {not(var_angka1 > var_angka2)}')