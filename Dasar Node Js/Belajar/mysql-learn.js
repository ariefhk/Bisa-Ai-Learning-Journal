const mysql = require("mysql");

const mydb = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "mysqljs",
});

mydb.connect((error) => {
  if (error) throw error;
  console.log("Berhasil melakukan koneksi");
});

// insert sql
const inset_query = () => {
  // Mendefinisikan query pada variable query
  var query =
    "INSERT INTO siswa (nisn, nama_siswa, alamat) VALUES ('90001', 'Arief Rachman Hakim', 'Lakboj')";

  // Eksekusi query
  mydb.query(query, (error, result) => {
    if (error) throw error;

    // Menampilkan pesan pada konsol
    console.log("Berhasil Memasukan Data!");
    console.log(result);
  });
};

// inset_query();

const selectData = () => {
  // Mendefinisikan query pada variable query
  var query = "SELECT * FROM SISWA";

  // Eksekusi Query
  mydb.query(query, (error, result) => {
    if (error) throw error;

    // Menampilkan pesan pada konsol
    console.log("Berhasil Mendapatkan Data");
    console.log(result);
  });
};

selectData();
mydb.end();
