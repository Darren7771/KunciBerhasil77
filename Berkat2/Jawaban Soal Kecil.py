# Awal Akhir
# 1. Fungsi untuk membuat kotak dengan karakter '#'
def buat_kotak(lebar, tinggi):
    """
    Membuat kotak berisi karakter '#' dengan lebar dan tinggi tertentu.
    Contoh untuk 3x3:
    # # #
    # # #
    # # #
    """
    for _ in range(tinggi):
        print("# " * lebar)  # Cetak setiap baris dengan '#' sebanyak 'lebar'
    print()  # Tambahkan baris kosong setelah kotak
 
# 2. Lanjutan Nomor 1, Fungsi untuk membuat kotak angka berurutan
def buat_kotak_angka(lebar, tinggi): 
    """
    Membuat kotak berisi angka berurutan dari 1 sampai lebar*tinggi.
    Contoh untuk 3x3:
    1 2 3
    4 5 6
    7 8 9
    """
    angka = 1  # Mulai dari angka 1
    for _ in range(tinggi):
        for _ in range(lebar):
            print(angka, end=" ")  # Cetak angka saat ini
            angka += 1  # Tambahkan 1 ke angka
        print()  # Baris baru setelah selesai satu baris
    print()  # Baris kosong tambahan

# 3. Lanjutan Nomor 2, Fungsi untuk membuat kotak angka dengan format 2 digit
def buat_kotak_angka_format(lebar, tinggi):
    """
    Membuat kotak angka dengan format 2 digit (01, 02, dst).
    Contoh untuk 3x3:
    01 02 03
    04 05 06
    07 08 09
    """
    angka = 1
    for _ in range(tinggi):
        for _ in range(lebar):
            print(f"{angka:02}", end=" ")  # Format angka menjadi 2 digit
            angka += 1
        print()
    print()

# 4. Lanjutan Nomor 3, Fungsi untuk membuat kotak dengan penanda "awal" dan "akhir"
def buat_kotak_awal_akhir(lebar, tinggi):
    """
    Membuat kotak dengan "awal" di posisi pertama dan "akhir" di posisi terakhir.
    Contoh untuk 3x3:
    awal 02 03
    04 05 06
    07 08 akhir
    """
    angka = 1
    akhir = lebar * tinggi  # Hitung posisi terakhir
    for _ in range(tinggi):
        for _ in range(lebar):
            if angka == 1:
                print("awal", end=" ")
            elif angka == akhir:
                print("akhir", end=" ")
            else:
                print(f"{angka:02}", end=" ")
            angka += 1
        print()
    print()

# 5. Lanjutan Nomor 4, Fungsi untuk membuat pola angka ular
def ular_angka(tinggi, lebar):
    """
    Membuat pola angka seperti ular (kiri-kanan, kanan-kiri).
    Contoh untuk 3x3:
    awal 02 03
    06 05 04
    07 08 akhir
    """
    angka = 1
    akhir = tinggi * lebar
    for baris in range(1, tinggi+1):
        if baris % 2 == 1:  # Baris ganjil (kiri ke kanan)
            for _ in range(lebar):
                if angka == 1:
                    print("awal", end=" ")
                elif angka == akhir:
                    print("akhir", end=" ")
                else:
                    print(f"{angka:02}", end=" ")
                angka += 1
            print()
        else:  # Baris genap (kanan ke kiri)
            temp = angka + lebar - 1
            for _ in range(lebar):
                if temp == 1:
                    print("awal", end=" ")
                elif temp == akhir:
                    print("akhir", end=" ")
                else:
                    print(f"{temp:02}", end=" ")
                temp -= 1
                angka += 1
            print()
    print()

# Pola Pusing
# 1. Fungsi untuk membuat pola angka menurun
def pola_menurun(lebar, tinggi):
    """
    Membuat pola angka menurun di setiap baris.
    Contoh untuk 5x5:
    5 4 3 2 1
    5 4 3 2 1
    5 4 3 2 1
    5 4 3 2 1
    5 4 3 2 1
    """
    for _ in range(tinggi):
        for j in range(lebar, 0, -1):  # Hitung mundur dari lebar ke 1
            print(j, end=" ")
        print()
    print()

# 2. Lanjutan Nomor 1, Fungsi untuk membuat pola angka menurun dengan offset baris
def pola_menurun_perbaris(lebar, tinggi):
    """
    Membuat pola angka menurun dengan pengurangan nilai per baris.
    Contoh untuk 5x5:
    5 4 3 2 1
    4 3 2 1 0
    3 2 1 0 -1
    2 1 0 -1 -2
    1 0 -1 -2 -3
    """
    for i in range(tinggi):
        for j in range(lebar, 0, -1):
            print(j - i, end=" ")  # Kurangkan indeks baris dari angka
        print()
    print() 

# 3. Lanjutan Nomor 2, Fungsi untuk membuat pola angka berbalik di angka 1
def pola_menurun_stop_di_1(lebar, tinggi):
    """
    Membuat pola angka yang berbalik arah setelah mencapai 1.
    Contoh untuk 5x5:
    5 4 3 2 1
    4 3 2 1 2
    3 2 1 2 3
    2 1 2 3 4
    1 2 3 4 5
    """
    for i in range(tinggi):
        for j in range(lebar, 0, -1):
            num = j - i
            if num < 1:  # Jika angka di bawah 1
                num = abs(num) + 2  # Ubah ke urutan positif
            print(num, end=" ")
        print()
    print()

# 4. Lanjutan Nomor 3, Fungsi untuk membuat pola angka diamond yang 1 ditengah (Maap ini emg ribet banget, tapi ak usahain)
# Kalo ga ngerti juga gapapa soal kek gini juga ga mungkin masuk pas uts (harusnya)
def pusing(tinggi, samping):
    """
    Membuat pola angka diamond (1 ditengah).
    Contoh untuk 5x5:
    5 4 3 4 5
    4 3 2 3 4
    3 2 1 2 3
    4 3 2 3 4
    5 4 3 4 5
    """
    # ==============================================
    # BAGIAN ATAS POLA (termasuk baris tengah)
    # ==============================================
    for baris in range(tinggi // 2 + 1):
        # Loop untuk bagian kiri diamond (nilai menurun)
        for kolom in range(samping, (samping // 2 + 1), -1):
            # Hitung nilai dasar: kolom - baris
            simpan = kolom - baris
            
            # Jika nilai >9, konversi ke 1 digit
            while simpan > 9:
                simpan %= 10
                
            print(simpan, end=" ")
        
        # Loop untuk bagian kanan diamond (nilai meningkat)
        for kolom in range((samping // 2 + 1), (samping + 1)):
            simpan = kolom - baris
            while simpan > 9:
                simpan %= 10
                
            # Format khusus untuk kolom terakhir    
            print(simpan, end=" " if kolom != 1 else "")
            
        print()  # Pindah baris setelah selesai satu baris

    # ==============================================
    # BAGIAN BAWAH POLA (mirror dari atas)
    # ==============================================    
    for baris in range(tinggi // 2):
        # Loop untuk bagian kiri diamond bawah
        for kolom in range((samping // 2 + 2), 1, -1):
            simpan = kolom + baris  # Nilai bertambah seiring baris
            while simpan > 9:
                simpan %= 10
            print(simpan, end=" ")
            
        # Loop untuk bagian kanan diamond bawah    
        for kolom in range((samping // 2), samping - 1):
            simpan = kolom + baris
            while simpan > 9:
                simpan %= 10
            print(simpan, end=" " if kolom != 1 else "")
        print()  # Pindah baris
