"""
unguided 5 

Kalkulator Rusak (DIGIT KIRI DIKALKULATOR)
kalkulatorRusak(3214,12,8235) = yang keambil cuma 3 , 1 , 8


"""
def kalkulatorRusak(angka1, angka2, angka3): 
    first_digit1 = angka1  
    while first_digit1 > 9: 
        first_digit1=first_digit1//10
    
    first_digit2 = angka2  
    while first_digit2 > 9: 
        first_digit2=first_digit2//10
    
    first_digit3 = angka3  
    while first_digit3 > 9: 
        first_digit3=first_digit3//10
    
        
    Hasil = first_digit1 * first_digit2 *first_digit3
    
    
    if angka1 == 0 or angka2 == 0 or angka3==0 :
        print("Error, angka tidak boleh 0")
    else: 
        print("Digit Kiri Angka1 :",first_digit1)
        print("Digit Kiri Angka2 :",first_digit2)
        print("Digit Kiri Angka3 :",first_digit3)
        print("Hasil :",Hasil)
    return " "

kalkulatorRusak(3214,12,8235)


"""""
Unguided 5 

Biaya dasar perawatan (sebelum faktor lainnya diterapkan):
Hatchback → Rp500.000
MPV → Rp800.000
Luxury → Rp2.000.000
Listrik → Rp500.000
Jika kendaraan menggunakan bahan bakar diesel, biaya dasar naik:
Hatchback: +10%
MPV: +15%
Luxury: +20%
Jika kendaraan berusia lebih dari 5 tahun, biaya dasar naik:
Hatchback: +10%
MPV: +20%
Luxury: +25%
Listrik: +10%
Biaya service berdasarkan tipe perawatan:
Perawatan rutin:
Hatchback → Rp75.000
MPV → Rp150.000
Luxury → Rp400.000
Listrik → Rp50.000
Perawatan darurat:
Hatchback → Rp150.000
MPV → Rp300.000
Luxury → Rp800.000
Listrik → Rp150.000
Biaya parkir kendaraan (biaya simpan mobil di bengkel) dihitung sebagai persentase dari harga kendaraan per hari:
Hatchback → 0.025% per hari
MPV → 0.03% per hari
Luxury → 0.067% per hari
Listrik → 0.02% per hari
Fungsi hitung_biaya_perawatan harus mengembalikan total biaya perawatan dalam bentuk integer (tanpa pembulatan desimal).

Catatan Penting: Pertambahan biaya persenan jangan pakai pecahan, pakai decimal. Contoh: 0.02 persen, berarti 0.0002*biaya_dasar, dan tanpa tanda kurung.

Jika inputan jenis kendaraan tidak valid, kembalikan "Jenis mobil tidak valid"

TEST CASE NYA : 
print(hitung_biaya_perawatan("Hatchback", 1000, "bensin", 6, "rutin", harga_kendaraan=200000000, waktu_parkir=3)) 
RESULT : 775000.0

"""""
def hitung_biaya_perawatan(jenis_mobil, jarak_tempuh, jenis_bahan_bakar, usia_mobil, tipe_perawatan, harga_kendaraan, biaya_tambahan=0, waktu_parkir=0):
    if jenis_mobil == "Hatchback":
        biaya_dasar = 500000
        if jenis_bahan_bakar == "diesel":
            biaya_dasar += biaya_dasar * 0.10
        if usia_mobil > 5:
            biaya_dasar += biaya_dasar * 0.10
        biaya_tambahan_perawatan = 75000 if tipe_perawatan == "rutin" else 150000
        biaya_keep = harga_kendaraan * 0.00025 * waktu_parkir
    elif jenis_mobil == "MPV":
        biaya_dasar = 800000
        if jenis_bahan_bakar == "diesel":
            biaya_dasar += biaya_dasar * 0.15
        if usia_mobil > 5:
            biaya_dasar += biaya_dasar * 0.20
        biaya_tambahan_perawatan = 150000 if tipe_perawatan == "rutin" else 300000
        biaya_keep = harga_kendaraan * 0.0003 * waktu_parkir
    elif jenis_mobil == "Luxury":
        biaya_dasar = 2000000
        if jenis_bahan_bakar == "diesel":
            biaya_dasar += biaya_dasar * 0.20
        if usia_mobil > 5:
            biaya_dasar += biaya_dasar * 0.25
        biaya_tambahan_perawatan = 400000 if tipe_perawatan == "rutin" else 800000
        biaya_keep = harga_kendaraan * 0.00067 * waktu_parkir
    elif jenis_mobil == "Listrik":
        biaya_dasar = 500000
        if usia_mobil > 5:
            biaya_dasar += biaya_dasar * 0.10
        biaya_tambahan_perawatan = 50000 if tipe_perawatan == "rutin" else 150000
        biaya_keep = harga_kendaraan * 0.0002 * waktu_parkir
    else:
        return "Jenis mobil tidak valid"
    
    biaya_total = biaya_dasar + biaya_tambahan_perawatan + biaya_tambahan + biaya_keep
    
    return biaya_total


"""""
TERNAK LELE ANDI 

Untuk itu, Andi perlu memperhatikan beberapa faktor yang akan mempengaruhi bisnisnya, antara lain:
1. Jumlah benih lele yang dibeli (dalam kg).
2. Harga beli benih lele per kg.
3. Harga jual lele per kg pada saat panen.
4. Biaya pakan selama sebulan.
5. Biaya Perawatan per minggu (yaitu obat-obatan).
6. Persentase lele berhasil bertumbuh (dalam 1 bulan)

RUMUS : 
Keuntungan Akhir =(Jumlah lele yang berhasil bertumbuh selama 3 bulan x Harga jual per kg) - (Total modal)
Jumlah lele yang berhasil tumbuh = (jumlah lele bulan sebelumnya) + (persentase keberhasil selama 1 bulan x jumlah lele bulan sebelumnya)
Total modal = (Total harga beli benih lele) + (total biaya pakan) + (total biaya perawatan)

Test Case 1
andiTernakLele(100,350_000,380_000,25_000,15_000,85)
output : "Rp. 205346749"
Test Case 2
print(andiTernakLele(50, 500_000, 300_000, 50_000, 20_000, 10))
output : "Merugi le"
Test Case 3
print(andiTernakLele(80, 400_000, 395_000, 30_000, 10_000, 35))
output : "Rp. 45537850"

1. Harus menggunakan fungsi bernama andiTernakLele yang menerima parameter :
    1. jumlah_benih : float
    2. harga_beli : int
    3. harga_jual : int
    4. biaya_pakan : int
    5. biaya_perawatan : int
    6. persentase keberhasilan : int
2. Fungsi harus mengembalikan satu nilai berupa string (total keuntungan Andi).
3. Persentase keberhasilan harus positif. Jika negatif maka mengeluarkan pesan "Persentase harus positif".


"""""

def andiTernakLele(jumlah_benih: float, harga_beli: int, harga_jual: int, 
                   biaya_pakan: int, biaya_perawatan: int, 
                   persentase_keberhasilan: int) -> str:
    if (persentase_keberhasilan>=0) :
        # Konversi persentase keberhasilan ke faktor pertumbuhan
        konversi_persentase=(persentase_keberhasilan)/100
        # Hitung total harga beli benih lele
        total_harga_beli = jumlah_benih * harga_beli

        # Hitung total biaya pakan selama 3 bulan
        total_biaya_pakan = biaya_pakan * 3

        # Hitung total biaya perawatan selama 3 bulan (4 minggu per bulan)
        total_biaya_perawatan = biaya_perawatan * 3 * 4

        # Hitung jumlah lele yang berhasil tumbuh setelah 3 bulan
        for _ in range(3):
            jumlah_benih = jumlah_benih+(jumlah_benih*konversi_persentase)

        # Hitung total modal
        total_modal = total_harga_beli + total_biaya_pakan + total_biaya_perawatan

        # Hitung total pendapatan dari hasil panen
        total_pendapatan = jumlah_benih * harga_jual

        # Hitung keuntungan akhir
        keuntungan = int(total_pendapatan - total_modal)

        return f"Rp. {keuntungan}" if keuntungan > 0 else "Merugi le"
    else:
        return "Persentase harus positif"