
import json
from datetime import datetime
import requests


def cariJadwalSholat(citycode):
    now = datetime.now()
    current_date = now.strftime('%Y/%m/%d')
    request_API = requests.get(
        f'https://api.myquran.com/v1/sholat/jadwal/{citycode}/{current_date}')

    data = request_API.text
    result_json = json.loads(data)
    print(f'Tanggal: {result_json["data"]["jadwal"]["date"]}')
    print(result_json["data"]["lokasi"])
    print(result_json["data"]["daerah"])
    print(f'-imsak : {result_json["data"]["jadwal"]["imsak"]}')
    print(f'-subuh : {result_json["data"]["jadwal"]["subuh"]}')
    print(f'-terbit: {result_json["data"]["jadwal"]["terbit"]}')
    print(f'-dhuha : {result_json["data"]["jadwal"]["dhuha"]}')
    print(f'-dzuhur: {result_json["data"]["jadwal"]["dzuhur"]}')
    print(f'-ashar : {result_json["data"]["jadwal"]["ashar"]}')
    print(f'-magrib: {result_json["data"]["jadwal"]["maghrib"]}')
    print(f'-isya  : {result_json["data"]["jadwal"]["isya"]}')


cari_kota = input('Masukan Lokasi: ')
request_cari_API = requests.get(
    f'https://api.myquran.com/v1/sholat/kota/cari/{cari_kota}')

data_cari = request_cari_API.text
resultCari_json = json.loads(data_cari)

if(str(resultCari_json['status']) == 'False'):
    print(resultCari_json['message'])
else:
    data_tempat = resultCari_json['data']
    data_length = len(data_tempat)
    city_code = ''
    for i in range(data_length):
        print(f'{i+1}:', data_tempat[i]['lokasi'])

    pilih_tempat = int(input('Masukan Pilihan [1/2..]: '))
    city_code += data_tempat[pilih_tempat-1]['id']
    cariJadwalSholat(city_code)
