# Program Manajemen Nilai Mahasiswa
# Menggunakan Dictionary untuk menyimpan data

# Dictionary untuk menyimpan data mahasiswa
data_mahasiswa = {}

def tampilkan_menu():
    """Menampilkan menu pilihan"""
    print("\n" + "="*50)
    print("PROGRAM MANAJEMEN NILAI MAHASISWA")
    print("="*50)
    print("1. Tambah Data")
    print("2. Ubah Data")
    print("3. Hapus Data")
    print("4. Tampilkan Data")
    print("5. Cari Data")
    print("6. Keluar")
    print("="*50)

def hitung_nilai_akhir(tugas, uts, uas):
    """Menghitung nilai akhir berdasarkan komponen"""
    return (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

def tambah_data():
    """Menambah data mahasiswa baru"""
    print("\n--- TAMBAH DATA ---")
    nama = input("Nama Mahasiswa: ")
    
    try:
        tugas = float(input("Nilai Tugas (30%): "))
        uts = float(input("Nilai UTS (35%): "))
        uas = float(input("Nilai UAS (35%): "))
        
        nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
        
        data_mahasiswa[nama] = {
            'tugas': tugas,
            'uts': uts,
            'uas': uas,
            'nilai_akhir': nilai_akhir
        }
        
        print(f"✓ Data {nama} berhasil ditambahkan!")
        print(f"  Nilai Akhir: {nilai_akhir:.2f}")
    except ValueError:
        print("✗ Error: Masukkan nilai berupa angka!")

def ubah_data():
    """Mengubah data mahasiswa yang sudah ada"""
    print("\n--- UBAH DATA ---")
    nama = input("Nama Mahasiswa yang akan diubah: ")
    
    if nama in data_mahasiswa:
        print(f"Data lama: {data_mahasiswa[nama]}")
        try:
            tugas = float(input("Nilai Tugas baru (30%): "))
            uts = float(input("Nilai UTS baru (35%): "))
            uas = float(input("Nilai UAS baru (35%): "))
            
            nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
            
            data_mahasiswa[nama] = {
                'tugas': tugas,
                'uts': uts,
                'uas': uas,
                'nilai_akhir': nilai_akhir
            }
            
            print(f"✓ Data {nama} berhasil diubah!")
            print(f"  Nilai Akhir baru: {nilai_akhir:.2f}")
        except ValueError:
            print("✗ Error: Masukkan nilai berupa angka!")
    else:
        print(f"✗ Data {nama} tidak ditemukan!")

def hapus_data():
    """Menghapus data mahasiswa"""
    print("\n--- HAPUS DATA ---")
    nama = input("Nama Mahasiswa yang akan dihapus: ")
    
    if nama in data_mahasiswa:
        del data_mahasiswa[nama]
        print(f"✓ Data {nama} berhasil dihapus!")
    else:
        print(f"✗ Data {nama} tidak ditemukan!")

def tampilkan_data():
    """Menampilkan semua data mahasiswa"""
    print("\n--- DAFTAR NILAI MAHASISWA ---")
    
    if not data_mahasiswa:
        print("Belum ada data mahasiswa.")
        return
    
    print("-"*80)
    print(f"{'No':<4} {'Nama':<20} {'Tugas':<8} {'UTS':<8} {'UAS':<8} {'Nilai Akhir':<12}")
    print("-"*80)
    
    for i, (nama, nilai) in enumerate(data_mahasiswa.items(), 1):
        print(f"{i:<4} {nama:<20} {nilai['tugas']:<8.2f} {nilai['uts']:<8.2f} "
              f"{nilai['uas']:<8.2f} {nilai['nilai_akhir']:<12.2f}")
    print("-"*80)

def cari_data():
    """Mencari data mahasiswa berdasarkan nama"""
    print("\n--- CARI DATA ---")
    nama = input("Nama Mahasiswa yang dicari: ")
    
    if nama in data_mahasiswa:
        nilai = data_mahasiswa[nama]
        print(f"\n✓ Data ditemukan:")
        print(f"  Nama        : {nama}")
        print(f"  Nilai Tugas : {nilai['tugas']:.2f}")
        print(f"  Nilai UTS   : {nilai['uts']:.2f}")
        print(f"  Nilai UAS   : {nilai['uas']:.2f}")
        print(f"  Nilai Akhir : {nilai['nilai_akhir']:.2f}")
    else:
        print(f"✗ Data {nama} tidak ditemukan!")

def main():
    """Fungsi utama program"""
    while True:
        tampilkan_menu()
        pilihan = input("\nPilih menu (1-6): ")
        
        if pilihan == '1':
            tambah_data()
        elif pilihan == '2':
            ubah_data()
        elif pilihan == '3':
            hapus_data()
        elif pilihan == '4':
            tampilkan_data()
        elif pilihan == '5':
            cari_data()
        elif pilihan == '6':
            print("\n✓ Terima kasih! Program selesai.")
            break
        else:
            print("\n✗ Pilihan tidak valid! Silakan pilih 1-6.")

# Jalankan program
if __name__ == "__main__":
    main()
