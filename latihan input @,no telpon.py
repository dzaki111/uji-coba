class Data:
    """
    Class untuk menyimpan data pendaftaran.
    """
    def __init__(self):
        self.records = []

    def add_record(self, record):
        """
        Menambahkan data pendaftaran ke dalam daftar.
        """
        self.records.append(record)

    def get_all_records(self):
        """
        Mengambil semua data pendaftaran.
        """
        return self.records


class View:
    """
    Class untuk menangani interaksi dengan pengguna.
    """
    @staticmethod
    def input_data():
        """
        Meminta input data dari pengguna.
        """
        try:
            nama = input("Masukkan nama lengkap: ")
            nomor_telepon = input("Masukkan nomor telepon: ")
            email = input("Masukkan email: ")
            return {"nama": nama, "nomor_telepon": nomor_telepon, "email": email}
        except Exception as e:
            print(f"Terjadi kesalahan saat memasukkan data: {e}")
            return None

    @staticmethod
    def show_records(records):
        """
        Menampilkan data pendaftaran dalam bentuk tabel sederhana.
        """
        if not records:
            print("Tidak ada data untuk ditampilkan.")
        else:
            print("+----+----------------------+-----------------+----------------------------+")
            print("| No | Nama Lengkap         | Nomor Telepon   | Email                      |")
            print("+----+----------------------+-----------------+----------------------------+")
            print("+----+----------------------+-----------------+----------------------------+")
        for i, rec in enumerate(records):
                print(f"| {i + 1:<10} | {rec['nama']:<10} | {rec['nomor_telepon']:<10} | {rec['email']:<10} |")

class Process:
    """
    Class untuk menangani logika validasi dan pengolahan data.
    """
    @staticmethod
    def validate_record(record):
        """
        Memvalidasi data pendaftaran.
        """
        try:
            if not record["nama"].replace(" ", "").isalpha():
                raise ValueError("Nama harus hanya berisi huruf dan spasi.")
            if not record["nomor_telepon"].isdigit() or len(record["nomor_telepon"]) < 10:
                raise ValueError("Nomor telepon harus hanya berisi angka dan minimal 10 digit.")
            if "@" not in record["email"] or "." not in record["email"].split("@")[-1]:
                raise ValueError("Email harus memiliki format yang benar (mengandung '@' dan domain).")
            return True
        except ValueError as e:
            print(f"Kesalahan validasi: {e}")
            return False


# Program utama
if __name__ == "__main__":
    data = Data()
    view = View()
    process = Process()

    while True:
        print("\n1. Tambahkan data")
        print("2. Tampilkan semua data")
        print("3. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            record = view.input_data()
            if record and process.validate_record(record):
                data.add_record(record)
                print("Data berhasil ditambahkan.")
            else:
                print("Data tidak valid, silakan coba lagi.")

        elif pilihan == "2":
            records = data.get_all_records()
            view.show_records(records)

        elif pilihan == "3":
            print("Program selesai. Terima kasih!")
            break

        else:
            print("Pilihan tidak valid, silakan pilih menu yang tersedia.")
