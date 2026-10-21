import tkinter as tk

def hasil_prediksi():
    var_hasil.set("Teknologi  Informasi")

top =tk.TK()
top.title("Aplikasi Prediksi Prodi Pilihan")
top.resizable(False, False)

lebar,tinggi = 520, 520
x = (top.winfo_screenwidth() - lebar) // 2
y = (top.winfo_screenwidth() - tinggi) // 2
top.geometry(f"{lebar}x{tinggi}+{x}+{y}")

label_judul = tk.tabel(
    top,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 18, "bold"),
)
label_judul.pack(pady=(20,10))