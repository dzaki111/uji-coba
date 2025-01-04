
# Program Pendaftaran Sederhana

## Deskripsi
Program ini adalah aplikasi pendaftaran sederhana berbasis teks yang memungkinkan pengguna untuk:
1. Menambahkan data pendaftaran berupa nama, nomor telepon, dan email.
2. Menampilkan semua data pendaftaran dalam format tabel.
3. Keluar dari program.

## Struktur Kelas dan Fungsinya

### 1. Kelas: `RegistrationData`
Berfungsi untuk mengelola penyimpanan dan pengambilan data pendaftaran.

#### Fungsi-fungsi:
- **`add_record(record)`**
  Menambahkan data pendaftaran baru ke dalam daftar.
  ```python
  def add_record(self, record):
      self.records.append(record)
  ```

- **`get_all_records()`**
  Mengembalikan semua data pendaftaran yang tersimpan.
  ```python
  def get_all_records(self):
      return self.records
  ```

---

### 2. Kelas: `UserInterface`
Mengelola interaksi dengan pengguna, termasuk menerima masukan dan menampilkan data.

#### Fungsi-fungsi:
- **`input_data()`**
  Meminta pengguna untuk memasukkan nama, nomor telepon, dan email. Mengembalikan data dalam bentuk kamus.
  ```python
  def input_data():
      try:
          nama = input("Masukkan nama lengkap: ")
          nomor_telepon = input("Masukkan nomor telepon: ")
          email = input("Masukkan email: ")
          return {"nama": nama, "nomor_telepon": nomor_telepon, "email": email}
      except Exception as e:
          print(f"Terjadi kesalahan saat memasukkan data: {e}")
          return None
  ```

- **`display_records(records)`**
  Menampilkan data pendaftaran dalam format tabel.
  ```python
  def display_records(records):
      if not records:
          print("Tidak ada data untuk ditampilkan.")
      else:
          print("+----+----------------------+-----------------+----------------------------+")
          print("| No | Nama Lengkap         | Nomor Telepon   | Email                      |")
          print("+----+----------------------+-----------------+----------------------------+")
          for i, rec in enumerate(records):
              print(f"| {i + 1:<2} | {rec['nama']:<20} | {rec['nomor_telepon']:<15} | {rec['email']:<26} |")
          print("+----+----------------------+-----------------+----------------------------+")
  ```

---

### 3. Kelas: `Validator`
Bertugas memvalidasi data pendaftaran yang dimasukkan pengguna.

#### Fungsi-fungsi:
- **`validate_data(data)`**
  Memvalidasi data sesuai aturan:
  - Nama hanya boleh berisi huruf dan spasi.
  - Nomor telepon harus berupa angka dengan minimal 10 digit.
  - Email harus memiliki format yang valid.
  ```python
  def validate_data(data):
      try:
          if not data["nama"].replace(" ", "").isalpha():
              raise ValueError("Nama harus hanya berisi huruf dan spasi.")
          if not data["nomor_telepon"].isdigit() or len(data["nomor_telepon"]) < 10:
              raise ValueError("Nomor telepon harus hanya berisi angka dan minimal 10 digit.")
          if "@" not in data["email"] or "." not in data["email"].split("@")[-1]:
              raise ValueError("Email harus memiliki format yang benar (mengandung '@' dan domain).")
          return True
      except ValueError as e:
          print(f"Kesalahan validasi: {e}")
          return False
  ```

---

## Alur Program Utama

### Pilihan Menu:
1. Tambahkan data.
2. Tampilkan semua data.
3. Keluar dari program.

### Menambahkan Data:
1. Program memanggil `UserInterface.input_data()` untuk meminta data.
2. Data divalidasi oleh `Validator.validate_data()`.
3. Jika valid, data ditambahkan ke `RegistrationData` menggunakan `add_record()`.

### Menampilkan Data:
1. Program memanggil `RegistrationData.get_all_records()` untuk mendapatkan data.
2. Data ditampilkan dalam format tabel oleh `UserInterface.display_records()`.

---

## Contoh Penggunaan

### Masukan:
```
1. Tambahkan data
2. Tampilkan semua data
3. Keluar
Pilih menu: 1
Masukkan nama lengkap: Alice
Masukkan nomor telepon: 0812345678
Masukkan email: alice@example.com
```

### Keluaran:
```
Data berhasil ditambahkan.
```

### Tampilkan Data:
```
1. Tambahkan data
2. Tampilkan semua data
3. Keluar
Pilih menu: 2
+----+----------------------+-----------------+----------------------------+
| No | Nama Lengkap         | Nomor Telepon   | Email                      |
+----+----------------------+-----------------+----------------------------+
| 1  | Alice                | 0812345678      | alice@example.com          |
+----+----------------------+-----------------+----------------------------+
```

---

## Lisensi
Program ini dibuat untuk tujuan pembelajaran dan bebas digunakan.
