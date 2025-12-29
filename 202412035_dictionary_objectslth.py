class Pelanggan:
    def __init__(self, id_pelanggan, nama, email):
        self.id_pelanggan = id_pelanggan
        self.nama = nama
        self.email = email

    def info(self):
        return f"{self.id_pelanggan} - {self.nama} ({self.email})"


# Dictionary untuk menyimpan objek pelanggan
data_pelanggan = {}


# Fungsi menambah pelanggan
def tambah_pelanggan(id_pelanggan, nama, email):
    if id_pelanggan in data_pelanggan:
        print("ID pelanggan sudah ada!")
    else:
        data_pelanggan[id_pelanggan] = Pelanggan(id_pelanggan, nama, email)
        print("Pelanggan berhasil ditambahkan.")


# Fungsi menghapus pelanggan
def hapus_pelanggan(id_pelanggan):
    if id_pelanggan in data_pelanggan:
        del data_pelanggan[id_pelanggan]
        print("Pelanggan berhasil dihapus.")
    else:
        print("Pelanggan tidak ditemukan.")


# Fungsi mencari pelanggan
def cari_pelanggan(id_pelanggan):
    if id_pelanggan in data_pelanggan:
        print("Pelanggan ditemukan:")
        print(data_pelanggan[id_pelanggan].info())
    else:
        print("Pelanggan tidak ditemukan.")


# Fungsi menampilkan seluruh pelanggan
def tampilkan_pelanggan():
    print("\n=== Daftar Pelanggan ===")
    if not data_pelanggan:
        print("Belum ada data pelanggan.")
    else:
        for pelanggan in data_pelanggan.values():
            print(pelanggan.info())


# ===== Contoh Eksekusi Program =====
tambah_pelanggan("PL001", "Andi", "andi@email.com")
tambah_pelanggan("PL002", "Budi", "budi@email.com")
tambah_pelanggan("PL003", "Citra", "citra@email.com")

tampilkan_pelanggan()

cari_pelanggan("PL002")

hapus_pelanggan("PL001")

tampilkan_pelanggan()
