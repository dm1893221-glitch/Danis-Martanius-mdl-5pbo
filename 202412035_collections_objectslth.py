class Buku:
    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

    def info(self):
        return f"'{self.judul}' oleh {self.penulis} ({self.tahun})"

# Membuat list of objects (berisi 5 objek buku)
daftar_buku = [
    Buku("Laskar Pelangi", "Andrea Hirata", 2005),
    Buku("Bumi", "Tere Liye", 2014),
    Buku("Filosofi Teras", "Henry Manampiring", 2018),
    Buku("Negeri 5 Menara", "A. Fuadi", 2009),
    Buku("Pulang", "Tere Liye", 2015)
]

# Menampilkan semua daftar buku
print("=== Daftar Seluruh Buku ===")
for bk in daftar_buku:
    print(bk.info())

# Implementasi fungsi mencari buku berdasarkan penulis
penulis_dicari = "Tere Liye"
print(f"\n=== Hasil Pencarian Penulis: {penulis_dicari} ===")

for bk in daftar_buku:
    if bk.penulis == penulis_dicari:
        print(bk.info())