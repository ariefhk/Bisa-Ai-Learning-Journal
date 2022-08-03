
# Import Library
import json
import subprocess
from datetime import datetime
import requests

# Fungsi untuk mendapatkan jadwal sholat berdasarkan city code


def waktuSholat(city_code):
    now = datetime.now()
    current_date = now.strftime("%Y/%m/%d")
    result = subprocess.run(["curl", f"https://api.myquran.com/v1/sholat/jadwal/{city_code}/{current_date}"],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result_json = json.loads(result.stdout)
    print(result_json["data"]["lokasi"])
    print(result_json["data"]["daerah"])
    print(f'Hari/Tanggal: {result_json["data"]["jadwal"]["tanggal"]}')
    print(f'- imsak {result_json["data"]["jadwal"]["imsak"]}')
    print(f'- subuh {result_json["data"]["jadwal"]["subuh"]}')
    print(f'- terbit {result_json["data"]["jadwal"]["terbit"]}')
    print(f'- dhuha {result_json["data"]["jadwal"]["dhuha"]}')
    print(f'- dzuhur {result_json["data"]["jadwal"]["dzuhur"]}')
    print(f'- ashar {result_json["data"]["jadwal"]["ashar"]}')
    print(f'- maghrib {result_json["data"]["jadwal"]["maghrib"]}')
    print(f'- isya {result_json["data"]["jadwal"]["isya"]}')


print('===== PROGRAM JADWAL SHOLAT MENGGUNAKAN PYTHON =====')
print('API : https://api.myquran.com/')
nama_kota = input('Masukan Lokasi Anda: ')  # mencari city code dengan inputan
result = subprocess.run(["curl", f"https://api.myquran.com/v1/sholat/kota/cari/{nama_kota}"],
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
result_json = json.loads(result.stdout)

# Error handling
if(str(result_json['status']) == "False"):  # status False dari API
    print('===== DATA TIDAK DITEMUKAN =====')
    # error message
    print(result_json['message'], ',Masukan data berdasarkan Kota/Kabupaten!')
else:
    print('===== DATA DITEMUKAN =====')
    daftar_data = len(result_json['data'])
    data_kota = ''
    for i in range(daftar_data):  # looping untuk menampilkan jumlah data yang ditemukan
        print(f'{i+1}:', result_json['data'][i]['lokasi'])

    # memilih city code dari inputan
    get_cityCode = int(input('Pilih Kota/Kabupaten [1/2/..]: '))
    data_kota += result_json['data'][get_cityCode-1]['id']
    waktuSholat(data_kota)  # panggil fungsi
