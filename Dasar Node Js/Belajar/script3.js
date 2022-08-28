const axios = require("axios");
const fs = require("fs");

const API_BASE_URL = "https://api.publicapis.org/entries?category=Weather";

async function get_api_list() {
  try {
    // Akses API dengan modul axios dengan keyword await
    let response = await axios.get(API_BASE_URL);

    // Mendapatkan data dari API
    let get_api = response.data["entries"];
    console.log("Berhasil mendapatkan data dari API");
    let api_list = "";
    get_api.forEach((item) => {
      let API_nama = item["API"];
      let API_deskripsi = item["Description"];
      let API_link = item["Link"];

      api_list += `Nama : ${API_nama}, Deskripsi : ${API_deskripsi}, Link : ${API_link}\n`;
    });
    // Memasukkan list API kedalam file CSV disertai keyword await
    await fs.writeFileSync("Api List -async_await.csv", api_list);

    console.log("Berhasil Memasukkan data ke CSV");
  } catch (error) {
    // Menampilkan ERROR
    console.log(`Gagal memasukkan data ke CSV ${error}`);
  }
}

get_api_list();
