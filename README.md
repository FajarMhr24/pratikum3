# Praktikum 3 - Tipe Data, Variable, dan Operator

Nama : Fajar maher habibillah

Kelas : TI.24.A.5

NIM : 312410549

Mata Kuliah : Bahasa Pemograman


## Mencari bilangan terbesar dari bilangan yang diinputkan
Program ini menentukan bilangan terbesar dari serangkaian bilangan yang diinputkan hingga input 0. Program ini menggunakan loop `while` dan kondisi `if` untuk memperbarui nilai terbesar yang ditemukan.

## Flowchart Program
![Foto](https://github.com/FajarMhr24/flochart/blob/bed00e29a4955786613abc593559239314794c8d/fc.2%2C3.png)

## kode Program
```python
maxBilangan = float('-inf')  
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
## penjelasan kode program

```python
maxBilangan = float('-inf')  
count = 0
```
`maxBilangan` diinisialisasi dengan minus tak hingga (`-∞`). Ini dilakukan agar bilangan pertama yang dimasukkan selalu lebih besar dan bisa menggantikan nilai awal tersebut.
`count` digunakan untuk menghitung jumlah bilangan valid yang dimasukkan.

```python
while True:
    print("Masukkan bilangan (0 untuk berhenti):")
    bilangan = int(input())  
```
Loop `while` True akan terus berjalan hingga pengguna memasukkan `0`.
Setiap kali loop berjalan, pengguna diminta memasukkan bilangan melalui `input()`.
Input dari pengguna dikonversi ke integer menggunakan `int()`.

```python
if bilangan == 0:
    break  
```
Jika pengguna memasukkan `0`, perintah break akan menghentikan loop dan program keluar dari proses `input`.

```python
if bilangan > maxBilangan:
    maxBilangan = bilangan  
```
Jika bilangan yang baru dimasukkan lebih besar dari `maxBilangan`, maka nilai `maxBilangan` diperbarui dengan bilangan tersebut.

```python
count += 1  
```
Setiap kali pengguna memasukkan bilangan (selain 0), `count` ditambah 1.

```python
if count > 0:
    print("Bilangan terbesar adalah:", maxBilangan)
else:
    print("Tidak ada bilangan yang dimasukkan.")
```
Setelah loop berhenti, program memeriksa apakah ada bilangan yang dimasukkan dengan melihat nilai `count`
   Jika `count > 0`, artinya ada bilangan yang dimasukkan, dan program menampilkan bilangan terbesar.
   Jika `count == 0`, artinya pengguna langsung memasukkan 0 tanpa input bilangan lain, dan program menampilkan pesan "Tidak ada bilangan yang dimasukkan."

## hasil kode program
![foto](Screenshot 2024-10-20 133035.png)
