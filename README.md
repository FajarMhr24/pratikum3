# Praktikum 3 - Tipe Data, Variable, dan Operator

Nama : Fajar maher habibillah

Kelas : TI.24.A.5

NIM : 312410549

Mata Kuliah : Bahasa Pemograman


## Mencari bilangan terbesar dari bilangan yang diinputkan
Program ini menentukan bilangan terbesar dari serangkaian bilangan yang diinputkan hingga input 0. Program ini menggunakan loop `while` dan kondisi `if` untuk memperbarui nilai terbesar yang ditemukan.

## Flowchart Program
![Foto](https://github.com/FajarMhr24/flochart/blob/bed00e29a4955786613abc593559239314794c8d/fc.2%2C3.png)

## Penjelasan kode Program
```python
maxBilangan = float('-inf')  # -∞
count = 0

while True:
    print("Masukkan bilangan (0 untuk berhenti):")
    bilangan = int(input())  

    if bilangan == 0:
        break  

    if bilangan > maxBilangan:
        maxBilangan = bilangan  

    count += 1 


if count > 0:
    print("Bilangan terbesar adalah:", maxBilangan)
else:
    print("Tidak ada bilangan yang dimasukkan.")

```

## hasil kode program
![foto](https://github.com/FajarMhr24/foto/blob/e1b13ed23644db24acabbe7fbfe633966a2327b5/Screenshot%202024-10-17%20204153.png)
