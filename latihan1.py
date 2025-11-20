# Program Daftar Kontak - Latihan 1

# 1. Buat Dictionary daftar kontak
# Nama sebagai key, dan nomor sebagai value
kontak = {
    "Ari": "081267888",
    "Dina": "087677770"
}

print("=== PROGRAM DAFTAR KONTAK ===\n")
print("1. Dictionary awal:")
print(kontak)
print()

# 2. Tampilkan kontaknya Ari
print("2. Kontak Ari:", kontak["Ari"])
print()

# 3. Tambah kontak baru dengan nama Riko, nomor 087654544
kontak["Riko"] = "087654544"
print("3. Setelah menambah Riko:")
print(kontak)
print()

# 4. Ubah kontak Dina dengan nomor baru 088999776
kontak["Dina"] = "088999776"
print("4. Setelah mengubah nomor Dina:")
print(kontak)
print()

# 5. Tampilkan semua Nama
print("5. Semua Nama:")
for nama in kontak.keys():
    print(f"   - {nama}")
print()

# 6. Tampilkan semua Nomor
print("6. Semua Nomor:")
for nomor in kontak.values():
    print(f"   - {nomor}")
print()

# 7. Tampilkan daftar Nama dan nomornya
print("7. Daftar Nama dan Nomor:")
for nama, nomor in kontak.items():
    print(f"   {nama:10} | {nomor}")
print()

# 8. Hapus kontak Dina
del kontak["Dina"]
print("8. Setelah menghapus kontak Dina:")
print(kontak)
print()

print("=== PROGRAM SELESAI ===")
