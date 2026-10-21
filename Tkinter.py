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

entries = []
for i, nama in enumerate(mapel):
    baris = i % 5          # 5 baris
    kolom = (i // 5) * 2   # 2 kolom (masing-masing label + entry)
    tk.Label(frame_input, text=nama + ":", anchor="w", width=16).grid(
        row=baris, column=kolom, sticky="w", padx=(0, 5), pady=6
    )
    e = tk.Entry(frame_input, width=8, bd=3, justify="center")
    e.grid(row=baris, column=kolom + 1, padx=(0, 25), pady=6)
    entries.append(e)

# BUTTON
tombol = tk.Button(
    top,
    text="Hasil Prediksi",
    font=("Arial", 12, "bold"),
    bg="#1a4f8b",
    fg="white",
    padx=20,
    pady=5,
    command=hasil_prediksi,
)
tombol.pack(pady=15)

var_hasil = tk.StringVar()
var_hasil.set("-") 

tk.Label(top, text="Prodi yang direkomendasikan:", font=("Arial", 11)).pack()
label_hasil = tk.Label(
    top,
    textvariable=var_hasil,
    font=("Arial", 16, "bold"),
    fg="#0b7a3b",
    relief=tk.RAISED,
    width=28,
    pady=8,
)
label_hasil.pack(pady=(5, 20))
top.mainloop()