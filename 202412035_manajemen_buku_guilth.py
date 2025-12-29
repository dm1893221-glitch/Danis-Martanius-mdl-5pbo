import tkinter as tk
from tkinter import ttk, messagebox, simpledialog


# ===== Class Tugas =====
# Class ini merepresentasikan satu tugas
class Tugas:
    def __init__(self, nama, status="Belum Selesai"):
        self.nama = nama
        self.status = status


# ===== Class Aplikasi To-Do List =====
class AplikasiTodoList:
    def __init__(self, root):
        self.root = root
        self.root.title("Manajemen Tugas (To-Do List)")
        self.root.geometry("500x400")

        # List of objects untuk menyimpan tugas
        self.daftar_tugas = []

        # ===== Frame Input =====
        frame_input = tk.Frame(root, padx=10, pady=10)
        frame_input.pack()

        tk.Label(frame_input, text="Nama Tugas:").grid(row=0, column=0, sticky=tk.W)
        self.entry_tugas = tk.Entry(frame_input, width=30)
        self.entry_tugas.grid(row=0, column=1, padx=5)

        tk.Button(
            frame_input,
            text="Tambah Tugas",
            command=self.tambah_tugas
        ).grid(row=0, column=2, padx=5)

        # ===== Frame Tombol =====
        frame_tombol = tk.Frame(root, padx=10, pady=10)
        frame_tombol.pack()

        tk.Button(frame_tombol, text="Edit", command=self.edit_tugas).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Hapus", command=self.hapus_tugas).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Tandai Selesai", command=self.tandai_selesai).pack(side=tk.LEFT, padx=5)

        # ===== Treeview =====
        frame_tabel = tk.Frame(root, padx=10, pady=10)
        frame_tabel.pack(fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(
            frame_tabel,
            columns=("Tugas", "Status"),
            show="headings"
        )
        self.tree.heading("Tugas", text="Tugas")
        self.tree.heading("Status", text="Status")
        self.tree.pack(fill=tk.BOTH, expand=True)

    # ===== Fungsi Tambah Tugas =====
    def tambah_tugas(self):
        nama = self.entry_tugas.get()

        if nama:
            tugas = Tugas(nama)
            self.daftar_tugas.append(tugas)
            self.tree.insert("", tk.END, values=(tugas.nama, tugas.status))
            self.entry_tugas.delete(0, tk.END)
        else:
            messagebox.showwarning("Peringatan", "Nama tugas tidak boleh kosong!")

    # ===== Fungsi Hapus Tugas =====
    def hapus_tugas(self):
        selected = self.tree.selection()
        if selected:
            index = self.tree.index(selected[0])
            self.tree.delete(selected[0])
            del self.daftar_tugas[index]
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas yang akan dihapus!")

    # ===== Fungsi Edit Tugas =====
    def edit_tugas(self):
        selected = self.tree.selection()
        if selected:
            index = self.tree.index(selected[0])
            tugas = self.daftar_tugas[index]

            nama_baru = simpledialog.askstring(
                "Edit Tugas",
                "Masukkan nama tugas baru:",
                initialvalue=tugas.nama
            )

            if nama_baru:
                tugas.nama = nama_baru
                self.tree.item(selected[0], values=(tugas.nama, tugas.status))
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas yang akan diedit!")

    # ===== Fungsi Tandai Selesai =====
    def tandai_selesai(self):
        selected = self.tree.selection()
        if selected:
            index = self.tree.index(selected[0])
            tugas = self.daftar_tugas[index]

            tugas.status = "Selesai"
            self.tree.item(selected[0], values=(tugas.nama, tugas.status))
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas terlebih dahulu!")


# ===== Program Utama =====
if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiTodoList(root)
    root.mainloop()
