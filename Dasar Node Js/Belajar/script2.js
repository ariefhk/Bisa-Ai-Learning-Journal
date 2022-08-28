const axios = require("axios");
const fs = require("fs");

const API_BASE_URL = "https://api.publicapis.org/entries?category=Weather";

axios
  .get(API_BASE_URL)
  // apabila promise terpenuhi akan masuk ke .then dibawah
  .then((response) => {
    console.log("Berhasil mendapatkan data dari API");

    // Mendapatkan data dari API
    let get_api = response.data["entries"];

    let api_list = "";
    get_api.forEach((item) => {
      let API_nama = item["API"];
      let API_deskripsi = item["Description"];
      let API_link = item["Link"];

      api_list += `Nama : ${API_nama}, Deskripsi : ${API_deskripsi}, Link : ${API_link}\n`;
    });

    // Memasukkan ke file CSV
    // Fungsi return dibawah ini memakai promise
    return fs.writeFileSync("Api List - promise.csv", api_list);
  });
