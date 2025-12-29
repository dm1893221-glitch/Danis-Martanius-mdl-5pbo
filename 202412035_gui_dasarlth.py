# Import library tkinter untuk membuat GUI
import tkinter as tk
# Import messagebox untuk menampilkan popup pesan
from tkinter import messagebox


# Membuat class AplikasiGUI
class AplikasiGUI:
    def __init__(self, root):
        # Menyimpan window utama
        self.root = root

        # Mengatur judul window
        self.root.title("Aplikasi GUI Sederhana")

        # Mengatur ukuran window
        self.root.geometry("300x200")

        # ===== Label =====
        # Label digunakan untuk menampilkan teks pada GUI
        self.label = tk.Label(root, text="Masukkan Nama Anda")
        self.label.pack(pady=10)

        # ===== Entry =====
        # Entry digunakan untuk menerima input teks dari user
        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=10)

        # ===== Button Tampilkan =====
        # Button ini berfungsi untuk menampilkan isi Entry
        self.button_tampil = tk.Button(
            root,
            text="Tampilkan",
            command=self.tampilkan_data  # Memanggil fungsi tampilkan_data
        )
        self.button_tampil.pack(pady=5)

        # ===== Button Hapus =====
        # Button ini berfungsi untuk menghapus isi Entry
        self.button_hapus = tk.Button(
            root,
            text="Hapus",
            command=self.hapus_data  # Memanggil fungsi hapus_data
        )
        self.button_hapus.pack(pady=5)

    # Fungsi untuk menampilkan isi Entry ke messagebox
    def tampilkan_data(self):
        # Mengambil teks dari Entry
        data = self.entry.get()

        # Mengecek apakah Entry tidak kosong
        if data:
            # Menampilkan data ke messagebox
            messagebox.showinfo("Hasil", f"Isi Entry: {data}")
        else:
            # Menampilkan peringatan jika Entry kosong
            messagebox.showwarning("Peringatan", "Entry masih kosong!")

    # Fungsi untuk menghapus isi Entry
    def hapus_data(self):
        # Menghapus teks dari Entry
        self.entry.delete(0, tk.END)


# Program utama
if __name__ == "__main__":
    # Membuat window utama
    root = tk.Tk()

    # Membuat objek dari class AplikasiGUI
    app = AplikasiGUI(root)

    # Menjalankan aplikasi GUI
    root.mainloop()
