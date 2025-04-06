""""

Permainan Huruf Aslijan dan Indah

Nilai 1 poin akan ditambahkan apabila terdapat huruf “i”,”I” (i uppercase) dan “l” (L lowercase).

Nilai 2 poin akan ditambahkan apabila terdapat huruf “Z” atau “z”.

Nilai 3 poin akan ditambahkan apabila terdapat huruf “E”.

Nilai 4 poin akan ditambahkan apabila terdapat huruf “A”.

Nilai 5 poin akan ditambahkan apabila terdapat huruf “S” atau “s”.

Nilai 6 poin akan ditambahkan apabila terdapat huruf “b”.

Nilai 7 poin akan ditambahkan apabila terdapat huruf “T”.

Nilai 8 poin akan ditambahkan apabila terdapat huruf “B”.

Nilai 9 poin akan ditambahkan apabila terdapat huruf “q”.

Nilai 10 poin akan ditambahkan apabila terdapat huruf “O” dan “o”

Nilai berdasarkan angka akan ditambahkan apabila terdapat angka dalam kalimat tersebut (dapat dilihat pada contoh 2)

Huruf lain, whitespace dan simbol apapun akan dihitung sebagai pengurangan penalti yang sudah ditentukan pada awal fungsi.
"""

def jumlahkanHuruf(kalimat, penalti):
    jumlah = 0
    jumlahPenalti = 0
    for i in kalimat:
        if i == "i" or i == "l" or i == "I":
            jumlah += 1
        elif i == "z" or i == "Z":
            jumlah += 2
        elif i == "E":
            jumlah += 3
        elif i == "A":
            jumlah += 4
        elif i == "s" or i == "S":
            jumlah += 5
        elif i == "b":
            jumlah += 6
        elif i == "T":
            jumlah += 7
        elif i == "B":
            jumlah += 8
        elif i == "q":
            jumlah += 9
        elif i == "o" or i == "O":
            jumlah += 10
        else:
            try:
                i = int(i)
                jumlah += i
            except:
                jumlahPenalti += penalti
    print(f"Nilai kalimat: {jumlah}")
    print(f"Jumlah penalti: {jumlahPenalti}")
    print(f"Nilai akhir: {jumlah - jumlahPenalti}")




# Digit Kiri Fibonacci

# Tony adalah seorang programmer berpengalaman. Ia telah menemukan banyak formula untuk membuat berbagai program, beberapa di antaranya adalah deret bilangan fibonacci dan pencarian digit kiri.
# Suatu hari, anaknya bertanya pada Tony tentang apa itu deret bilangan fibonacci. Tony-pun menjelaskan bahwa deret bilangan fibonacci adalah suatu rangkaian bilangan di mana setiap bilangannya adalah jumlah dari dua bilangan sebelumnya. Contohnya :

# 1 1 2 3 5 8

# (2 berasal dari 1+1)
# (3 berasal dari 2+1)
# (5 berasal dari 3+2)
# (8 berasal dari 5+3)

# Anaknya-pun kembali bertanya pada Tony tentang algoritma pencarian digit kiri. Tony-pun kembali menjelaskan bahwa kita bisa mendapatkan digit paling kiri dari suatu bilangan dengan menggunakan pembagian bulat ( // ) terhadap 10 secara berulang hingga bilangan tersebut kurang dari 10. Contohnya :

# 125

# (125 dibagi 10 secara bulat akan menghasilkan 12)
# (12 dibagi 10 secara bulat akan menghasilkan 1)
# (1 adalah digit kiri dari 125)

# Setelah menjelaskan kepada anaknya, tiba-tiba Tony mendapat suatu ide. Ia berpikir untuk menggabungkan algoritma deret bilangan fibonacci dengan algoritma pencarian digit kiri, untuk menghasilkan suatu program yang dapat mendeteksi digit kiri dalam suatu deret bilangan fibonacci. Tony menamai-nya sebagai program Digit Kiri Fibonacci. 

# Tugas kalian adalah membantu Tony untuk membuat program tersebut.

# Buatlah fungsi digitKiriFibonacci() yang memiliki parameter n. Tujuan dari fungsi ini adalah untuk menampilkan deret bilangan fibonacci sekaligus mendeteksi digit kiri dalam deret bilangan fibonacci tersebut. 
# Fungsi Digit Kiri Fibonacci ini akan menampilkan 2 output, yaitu : 
# a.           Deret bilangan fibonacci.
# b.           Digit kiri yang ada dalam deret bilangan fibonacci tersebut.
# Perlu diingat bahwa n tidak boleh sama dengan 1 atau kurang dari 1. Buatlah agar sistem dapat mengeluarkan output berupa pesan error “n tidak valid!” ketika n = 1 atau n < 1.

# Penjelasan Parameter:
# Hanya terdapat 1 parameter pada fungsi ini, nama parameter tidak harus disamakan dengan contoh.
# n = Tipe data Integer, Memberikan suatu angka dengan nilai minimal adalah 2. Ingat, parameter ini tidak boleh sama dengan 1 atau kurang dari 1. Jika iya, maka buatlah pesan error seperti yang sudah dijelaskan di atas.
# Catatan Tambahan:
# ·         Mohon BACA SOAL terlebih dahulu, apabila masih tidak jelas baru ditanyakan kepada asdos.
# ·         Fungsi ini tidak melakukan return (langsung print)
# ·         WAJIB menggunakan fungsi while loop atau for loop.
# ·         Perhatikan lagi huruf kapital dan format output yang diminta (ini case-sensitive, jadi beda 1 karakter atau beda spasi bisa salah, hati-hati!)


def digitKiriFibonacci(n):
    if n<=1:
        print("n tidak valid!")
    
    else:
        # ini untuk menampilkan deret fibonacci
        print("Deret Fibonacci : ", end="")
        fn1 = 1
        fn2 = 1
        print(fn1, end=" ")
        print(fn2, end=" ")

        for i in range(n-2):
            fn3 = fn1 + fn2
            print(fn3, end=" ")
            fn1 = fn2
            fn2 = fn3
        
        print()

        # ini untuk menampilkan digit kiri deret fibonacci
        print("Digit Kiri : ", end="")
        fn1 = 1
        fn2 = 1
        print(fn1, end=" ")
        print(fn2, end=" ")

        for i in range(n-2):
            fn3 = fn1 + fn2
            kiri = fn3
            if kiri < 10:
                print(fn3, end=" ")
            else:
                while kiri > 10:
                    kiri = kiri // 10
                print(kiri, end=" ")
            fn1 = fn2
            fn2 = fn3





# HITUNG ANGKA VOKAL 
# print(hitung_vokal("Hari ini hari senin.")) ==> Jumlah Huruf Vokal: 8

def hitung_vokal(kalimat):
    hasil = 0
    for i in kalimat:
        if i == "a" or i == "i" or i == "u" or i == "e" or i == "o" or i == "A" or i == "I" or i == "U" or i == "E" or i == "O":
            hasil += 1     
    if hasil == 0:
        return ("Tidak Ada Huruf Vokal pada kalimat Itu")
    return ("Jumlah Huruf Vokal: " + str(hasil))






# Deret GWS
# Di suatu pagi yang cerah di Sekolah Baktiojo, sang guru matematika memberikan sebuah tugas harian kepada murid-muridnya. Tugas harian tersebut adalah menuliskan deret kelipatan bilangan. Ikin merasa tugas tersebut terlalu mudah untuk dikerjakan secara manual, jadi dia membuat program untuk tugas tersebut, tetapi dengan tambahan fitur. Fitur yang dikembangkan Ikin adalah menggantikan bilangan kelipatan tertentu dengan kata tertentu.

# Ikin membuat sebuah fungsi bernama deret_gws. Fungsi tersebut menerima 7 parameter: jumlah_bilangan, kelipatan, angka_gws1, angka_gws2, kata_gws1, kata_gws2, kata_gws_spesial. Jumlah_bilangan adalah berapa banyak bilangan kelipatan yang mau ditampilkan. Kelipatan menentukan kelipatan deret bilangan yang ditampilkan. Parameter angka_gws1 dan angka_gws2, kata_gws1, kata_gws2, dan kata_spesial adalah parameter tambahan untuk fitur yang dikembangkan Ikin.

# Cara kerja deret bilangan yang dikembangkan oleh Ikin adalah menampilkan deret bilangan berkelipatan, dan menggantikan bilangan kelipatan tertentu dengan kata yang diberikan. Bilangan yang merupakan kelipatan angka_gws1 akan menampilkan kata_gws1, bilangan kelipatan angka_gws2 menampilkan kata_gws2, dan ketika bilangan adalah kelipatan angka_gws1 dan angka_gws2, program akan menampilkan kata_spesial. Semua hasil deret bilangan tersebut ditampilkan dalam 1 baris.

# Ketentuan Deret BIlangan GWS
# Ada dalam cerita diatas.

# Dan ada dalam penjelasan parameter di bawah.

# Penjelasan Parameter:
# Ada 7 parameter untuk fungsi ini. Parameter jumlah_bilangan, kelipatan, angka_gws1, dan angka_gws2  harus berupa bilangan bulat positif. Angka_gws1 dan angka_gws 2 harus bernilai lebih kecil atau sama dengan jumlah_bilangan. Kata_gws1, kata_gws2, dan kata_spesial harus berupa string. Apabila input parameter tidak memenuhi kriteria, maka fungsi harus menampilkan pesan "TIDAK VALID”. Nama parameter harus sesuai dengan ketentuan.

# Format : 
# jumlah_bilangan = Menentukan berapa banyak bilangan kelipatan yang mau ditampilkan

# kelipatan = Menentukan kelipatan deret bilangan

# angka_gws1 = Menentukan kapan hasil perkalian harus digantikan kata_gws1

# angka_gws2 = Menentukan kapan hasil perkalian harus digantikan kata_gws2

# kata_gws1 = Kata untuk menggantikan hasil perkalian yang habis dibagi angka_gws1 saja.

# kata_gws2 = Kata untuk menggantikan hasil perkalian yang habis dibagi angka_gws2 saja.

# kata_spesial = Kata untuk menggantikan hasil perkalian yang habis dibagi angka_gws1 dan angka_gws2

# deret_gws(20,2,3,5,"halo","hai","bye") == >> 2 4 halo 8 hai halo 14 16 halo hai 22 halo 26 28 bye 32 34 halo 38 hai 
# deret_gws(30,1,5,10,"DOR","BOOM","DUAR") == >> 1 2 3 4 DOR 6 7 8 9 DUAR 11 12 13 14 DOR 16 17 18 19 DUAR 21 22 23 24 DOR 26 27 28 29 DUAR

def deret_gws(jumlah_bilangan, kelipatan, angka_gws1, angka_gws2, kata_gws1, kata_gws2, kata_gws_spesial):
    try:
        if jumlah_bilangan > 0 and kelipatan > 0 and angka_gws1 <= jumlah_bilangan and angka_gws2 <= jumlah_bilangan:
            for i in range(1,jumlah_bilangan +1):
                if i*kelipatan % angka_gws1 == 0 and i*kelipatan % angka_gws2 == 0:
                    print(kata_gws_spesial, end=" ")
                elif i*kelipatan % angka_gws1 == 0:
                    print(kata_gws1, end=" ")
                elif i*kelipatan % angka_gws2 ==0:
                    print(kata_gws2, end=" ")
                else:
                    print(i*kelipatan, end=" ")
        else:
            print("TIDAK VALID")
    except TypeError:
        print("TIDAK VALID")
    return 0
