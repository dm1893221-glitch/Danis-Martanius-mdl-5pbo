import tkinter as tk
from tkinter import ttk, messagebox, filedialog

# =========================
# CLASS MAHASISWA
# =========================
class Mahasiswa:
    """
    Class Mahasiswa untuk menyimpan data mahasiswa
    """
    def __init__(self, nim, nama, jurusan, ipk):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan
        self.ipk = float(ipk)

    def info(self):
        """
        Mengembalikan informasi mahasiswa dalam bentuk tuple
        """
        return (self.nim, self.nama, self.jurusan, self.ipk)

    def update_ipk(self, ipk):
        """
        Mengupdate nilai IPK mahasiswa
        """
        self.ipk = float(ipk)


# =========================
# CLASS APLIKASI GUI
# =========================
class AplikasiMahasiswa:
    def __init__(self, root):
        self.root = root
        self.root.title("Manajemen Mahasiswa")
        self.root.geometry("750x500")

        # Dictionary untuk menyimpan objek mahasiswa (key = NIM)
        self.data_mahasiswa = {}

        # =========================
        # FRAME INPUT DATA
        # =========================
        frame_input = tk.LabelFrame(root, text="Input Data Mahasiswa", padx=10, pady=10)
        frame_input.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(frame_input, text="NIM").grid(row=0, column=0, sticky=tk.W)
        tk.Label(frame_input, text="Nama").grid(row=1, column=0, sticky=tk.W)
        tk.Label(frame_input, text="Jurusan").grid(row=2, column=0, sticky=tk.W)
        tk.Label(frame_input, text="IPK").grid(row=3, column=0, sticky=tk.W)

        self.entry_nim = tk.Entry(frame_input)
        self.entry_nama = tk.Entry(frame_input)
        self.entry_jurusan = tk.Entry(frame_input)
        self.entry_ipk = tk.Entry(frame_input)

        self.entry_nim.grid(row=0, column=1, pady=3)
        self.entry_nama.grid(row=1, column=1, pady=3)
        self.entry_jurusan.grid(row=2, column=1, pady=3)
        self.entry_ipk.grid(row=3, column=1, pady=3)

        # =========================
        # TOMBOL CRUD
        # =========================
        frame_button = tk.Frame(root)
        frame_button.pack(pady=5)

        tk.Button(frame_button, text="Tambah", width=12, command=self.tambah).pack(side=tk.LEFT, padx=3)
        tk.Button(frame_button, text="Update", width=12, command=self.update).pack(side=tk.LEFT, padx=3)
        tk.Button(frame_button, text="Hapus", width=12, command=self.hapus).pack(side=tk.LEFT, padx=3)
        tk.Button(frame_button, text="Cari", width=12, command=self.cari).pack(side=tk.LEFT, padx=3)

        # =========================
        # TREEVIEW (TAMPILAN DATA)
        # =========================
        frame_table = tk.Frame(root)
        frame_table.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.tree = ttk.Treeview(
            frame_table,
            columns=("NIM", "Nama", "Jurusan", "IPK"),
            show="headings"
        )

        self.tree.heading("NIM", text="NIM")
        self.tree.heading("Nama", text="Nama")
        self.tree.heading("Jurusan", text="Jurusan")
        self.tree.heading("IPK", text="IPK")

        self.tree.pack(fill=tk.BOTH, expand=True)

        # =========================
        # FITUR TAMBAHAN
        # =========================
        frame_extra = tk.Frame(root)
        frame_extra.pack(pady=5)

        tk.Button(frame_extra, text="Rata-rata IPK", command=self.rata_ipk).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_extra, text="IPK Tertinggi", command=self.ipk_tertinggi).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_extra, text="Filter Jurusan", command=self.filter_jurusan).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_extra, text="Export File", command=self.export_file).pack(side=tk.LEFT, padx=5)

    # =========================
    # FUNGSI CRUD
    # =========================
    def tambah(self):
        """
        Menambahkan data mahasiswa ke dictionary dan Treeview
        """
        nim = self.entry_nim.get()
        nama = self.entry_nama.get()
        jurusan = self.entry_jurusan.get()
        ipk = self.entry_ipk.get()

        # Validasi input
        if not nim or not nama or not jurusan or not ipk:
            messagebox.showwarning("Peringatan", "Semua data harus diisi!")
            return

        if nim in self.data_mahasiswa:
            messagebox.showerror("Error", "NIM sudah terdaftar!")
            return

        try:
            mahasiswa = Mahasiswa(nim, nama, jurusan, ipk)
        except ValueError:
            messagebox.showerror("Error", "IPK harus berupa angka!")
            return

        self.data_mahasiswa[nim] = mahasiswa
        self.tree.insert("", tk.END, values=mahasiswa.info())
        self.clear_entry()

    def update(self):
        """
        Mengupdate data IPK mahasiswa
        """
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Peringatan", "Pilih data terlebih dahulu!")
            return

        nim = self.tree.item(selected[0])["values"][0]
        ipk_baru = self.entry_ipk.get()

        try:
            self.data_mahasiswa[nim].update_ipk(ipk_baru)
            self.tree.item(selected[0], values=self.data_mahasiswa[nim].info())
        except ValueError:
            messagebox.showerror("Error", "IPK harus angka!")

    def hapus(self):
        """
        Menghapus data mahasiswa
        """
        selected = self.tree.selection()
        if not selected:
            return

        nim = self.tree.item(selected[0])["values"][0]
        del self.data_mahasiswa[nim]
        self.tree.delete(selected[0])

    def cari(self):
        """
        Mencari mahasiswa berdasarkan NIM atau Nama
        """
        keyword = self.entry_nama.get().lower()
        for item in self.tree.get_children():
            self.tree.delete(item)

        for mhs in self.data_mahasiswa.values():
            if keyword in mhs.nim.lower() or keyword in mhs.nama.lower():
                self.tree.insert("", tk.END, values=mhs.info())

    # =========================
    # FITUR TAMBAHAN
    # =========================
    def rata_ipk(self):
        """
        Menghitung rata-rata IPK
        """
        if not self.data_mahasiswa:
            return
        rata = sum(m.ipk for m in self.data_mahasiswa.values()) / len(self.data_mahasiswa)
        messagebox.showinfo("Rata-rata IPK", f"Rata-rata IPK: {rata:.2f}")

    def ipk_tertinggi(self):
        """
        Menampilkan mahasiswa dengan IPK tertinggi
        """
        mhs = max(self.data_mahasiswa.values(), key=lambda x: x.ipk)
        messagebox.showinfo("IPK Tertinggi", f"{mhs.nama} ({mhs.ipk})")

    def filter_jurusan(self):
        """
        Filter mahasiswa berdasarkan jurusan
        """
        jurusan = self.entry_jurusan.get().lower()
        for item in self.tree.get_children():
            self.tree.delete(item)

        for mhs in self.data_mahasiswa.values():
            if jurusan in mhs.jurusan.lower():
                self.tree.insert("", tk.END, values=mhs.info())

    def export_file(self):
        """
        Export data ke file teks
        """
        file = filedialog.asksaveasfilename(defaultextension=".txt")
        if not file:
            return

        with open(file, "w") as f:
            for mhs in self.data_mahasiswa.values():
                f.write(f"{mhs.nim}, {mhs.nama}, {mhs.jurusan}, {mhs.ipk}\n")

        messagebox.showinfo("Sukses", "Data berhasil diexport!")

    def clear_entry(self):
        """
        Mengosongkan input
        """
        self.entry_nim.delete(0, tk.END)
        self.entry_nama.delete(0, tk.END)
        self.entry_jurusan.delete(0, tk.END)
        self.entry_ipk.delete(0, tk.END)


# =========================
# MAIN PROGRAM
# =========================
if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiMahasiswa(root)
    root.mainloop()
