# Inisialisasi variabel
maxBilangan = float('-inf')  # -∞
count = 0

# Loop utama untuk menerima input pengguna
while True:
    print("Masukkan bilangan (0 untuk berhenti):")
    bilangan = int(input())  # Input bilangan

    if bilangan == 0:
        break  # Keluar dari loop jika input adalah 0

    if bilangan > maxBilangan:
        maxBilangan = bilangan  # Update bilangan terbesar

    count += 1  # Tambah hitungan bilangan yang dimasukkan

# Mengecek apakah ada bilangan yang dimasukkan
if count > 0:
    print("Bilangan terbesar adalah:", maxBilangan)
else:
    print("Tidak ada bilangan yang dimasukkan.")
