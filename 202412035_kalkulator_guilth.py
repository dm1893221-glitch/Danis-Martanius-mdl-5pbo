import tkinter as tk
from tkinter import messagebox


class KonversiSuhuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Konversi Suhu")
        self.root.geometry("300x200")

        # ===== Label =====
        self.label = tk.Label(root, text="Masukkan Suhu (Celsius)")
        self.label.pack(pady=10)

        # ===== Entry =====
        self.entry_celsius = tk.Entry(root, width=25)
        self.entry_celsius.pack(pady=5)

        # ===== Button Konversi =====
        self.button_konversi = tk.Button(
            root,
            text="Konversi ke Fahrenheit",
            command=self.konversi_suhu
        )
        self.button_konversi.pack(pady=5)

        # ===== Label Hasil =====
        self.label_hasil = tk.Label(root, text="Hasil: -")
        self.label_hasil.pack(pady=10)

    # Fungsi konversi suhu
    def konversi_suhu(self):
        nilai = self.entry_celsius.get()

        # Validasi input
        if nilai == "":
            messagebox.showwarning("Peringatan", "Input tidak boleh kosong!")
            return

        try:
            celsius = float(nilai)
            fahrenheit = (celsius * 9 / 5) + 32
            self.label_hasil.config(
                text=f"Hasil: {fahrenheit:.2f} °F"
            )
        except ValueError:
            messagebox.showerror(
                "Error",
                "Masukkan angka yang valid!"
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = KonversiSuhuGUI(root)
    root.mainloop()
