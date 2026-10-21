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

frame_input = tk.LabelFrame(
    top, text=" Masukkan Nilai Mata Pelajaran ", font=("Arial", 11, "bold"),
    padx=20, pady=15,
)
frame_input.pack(padx=25, pady=10, fill="x")

mapel = [
    "Matematika", "Bahasa Indonesia", "Bahasa Inggris", "Fisika", "Kimia",
    "Biologi", "Ekonomi", "Sejarah", "Geografi", "Informatika",
]