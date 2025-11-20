# Praktikum5
# Program Manajemen Nilai Mahasiswa

Program ini digunakan untuk mengelola data nilai mahasiswa menggunakan bahasa Python.  
Data disimpan dalam bentuk **dictionary**, dan pengguna dapat menambah, mengubah, menghapus, menampilkan, serta mencari data mahasiswa. Program berjalan menggunakan menu interaktif.

---

## Fitur Program
1. **Tambah Data Mahasiswa**  
   Menginput nama, nilai tugas, UTS, dan UAS, kemudian menghitung nilai akhir berdasarkan:
   - Tugas: 30%
   - UTS: 35%
   - UAS: 35%

2. **Ubah Data Mahasiswa**  
   Memperbarui data nilai mahasiswa yang sudah ada.

3. **Hapus Data**  
   Menghapus data mahasiswa berdasarkan nama.

4. **Tampilkan Semua Data**  
   Menampilkan seluruh data dalam bentuk tabel sederhana.

5. **Cari Data Mahasiswa**  
   Mencari data berdasarkan nama mahasiswa.

6. **Keluar Program**

---

## Struktur Program
Program terdiri dari beberapa fungsi utama:

- `tampilkan_menu()`  
  Menampilkan menu pilihan utama.

- `tambah_data()`  
  Menambahkan data mahasiswa baru.

- `ubah_data()`  
  Mengubah data mahasiswa yang sudah tersimpan.

- `hapus_data()`  
  Menghapus data mahasiswa tertentu.

- `tampilkan_data()`  
  Menampilkan seluruh daftar nilai mahasiswa.

- `cari_data()`  
  Mencari data berdasarkan nama.

- `hitung_nilai_akhir()`  
  Menghitung nilai akhir berdasarkan bobot.

- `main()`  
  Menjalankan program menggunakan loop menu.

---

## Cara Menjalankan Program
1. Pastikan Python sudah terinstal.
2. Simpan file dengan nama `nilai_mahasiswa.py` (atau sesuai keinginan).
3. Jalankan program dengan perintah:
   ```bash
   python nilai_mahasiswa.py
