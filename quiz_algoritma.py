# ============================================
# Quiz Algoritma Python
# Input - Percabangan - Perulangan (while)
# ============================================

# Data target nilai setiap mahasiswa
data_mahasiswa = {
    "Andi": 70,
    "Budi": 75,
    "Citra": 80
}

# === 1. Input nama mahasiswa ===
print("=" * 45)
print("   PROGRAM UJIAN MATEMATIKA MAHASISWA")
print("=" * 45)
print("\nDaftar Mahasiswa dan Target Nilai:")
for nama, target in data_mahasiswa.items():
    print(f"  - {nama} : {target}")

nama_input = input("\nMasukkan nama mahasiswa: ")

# === Cek apakah nama ada di data ===
if nama_input in data_mahasiswa:
    target_nilai = data_mahasiswa[nama_input]
    print(f"\nNama  : {nama_input}")
    print(f"Target Nilai : {target_nilai}")
    print("-" * 35)

    # === 2 & 3. Input nilai dan perulangan while (maks 3 kali) ===
    percobaan = 1
    lulus = False

    while percobaan <= 3 and not lulus:
        nilai = int(input(f"Nilai {percobaan} : "))

        # Pengecekan terhadap target nilai
        if nilai >= target_nilai:
            lulus = True
        else:
            if percobaan < 3:
                print(f"  -> Nilai belum mencapai target ({target_nilai}). Silakan coba lagi.")
            percobaan += 1

    # === 4. Tampilkan hasil akhir ===
    print("-" * 35)
    if lulus:
        print(f"\n{nama_input} berhasil lulus setelah {percobaan} kali percobaan!")
    else:
        print(f"\n{nama_input} tidak lulus setelah 3 kali percobaan!")

else:
    print(f"\nMaaf, nama '{nama_input}' tidak ditemukan dalam daftar mahasiswa.")
    print("Nama yang tersedia: Andi, Budi, Citra")