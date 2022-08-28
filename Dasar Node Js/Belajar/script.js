const request = require("request");
const fs = require("fs");

const API_BASE_URL = "https://api.publicapis.org/entries?category=Weather";

// Fungsi Request dan Callback Func
request(API_BASE_URL, (error, response, body) => {
  // Check Error
  if (error) {
    console.error(`Gagal akses API : ${error.message}`);
    return;
  }

  // Check Status Code 200 / tidak
  if (response.statusCode != 200) {
    console.error(`Gagal akses API, Status Code : ${response.statusCode}`);
    return;
  }

  // Jika tidak error maka data di body diubah menjadi JSON
  console.log("Proses List API");
  let get_api = JSON.parse(body)["entries"];

  // Membuat list api untuk dimasukkan ke CSV
  let api_list = "";
  get_api.forEach((item) => {
    let API_nama = item["API"];
    let API_deskripsi = item["Description"];
    let API_link = item["Link"];

    api_list += `Nama : ${API_nama}, Deskripsi : ${API_deskripsi}, Link : ${API_link}\n`;
  });

  // Memasukan data ke CSV
  fs.writeFileSync("Api_list.csv", api_list, (error) => {
    if (error) {
      console.log(`Gagal memasukkan ke CSV: ${error}`);
      return;
    }

    console.log("Berhasil memasukkan data ke csv");
  });
  console.log(api_list);
});
