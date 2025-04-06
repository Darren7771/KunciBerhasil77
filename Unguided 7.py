"""
segitigaPensiunPersegiGajian(6) 
* * * * * * 
  * * * * * 
    * * * * 
      * * * 
        * * 
          * 
# * # * # * 
* * * * * * 
# * # * # * 
* * * * * * 
# * # * # * 
* * * * * * 

segitigaPensiunPersegiGajian(-1)
"N iTu Tidakssssssssss Validddd Gusesssss"

"""

def segitigaPensiunPersegiGajian(n):
    if n < 0:
        print("\"N iTu Tidakssssssssss Validddd Gusesssss\"")
    
    for i in range(n,0,-1):
        for j in range(n):
            if j <= n - i - 1 :
                print(" ", end=" ")
            else:
                print("*", end=" ")
        print("")
    
    for k in range(0, n):
        for l in range(0,n):
            if k %2==1:
                print("*", end=" ")
            elif l%2==1:
                print("*", end=" ")
            elif k % 2==0:
                print("#", end=" ")
            
        print("")
        


"""
Tabel Perkalian Nggak Jelas
Di suatu pagi yang cerah di Sekolah Baktiojo, sang guru matematika memberikan sebuah tugas harian kepada murid-muridnya. Tugas harian tersebut adalah membuat tabel perkalian. Jaeman malas untuk mengerjakan tugas tersebut, sehingga dia menulis sebuah program untuk membuat tabel perkalian. Dia meminta bantuan Ikin, temannya, untuk membuat program tersebut.

Mereka membuat sebuah fungsi bernama tabel_perkalian_spesial. Fungsi tersebut menerima 2 parameter: baris dan kolom. Parameter tinggi digunakan untuk menentukan jumlah baris tabel dan parameter panjang digunakan untuk menentukan jumlah kolom tabel. 

Setelah Jaeman menyelesaikan program tersebut, Jaeman tidur. Melihat temannya tidur, Ikin iseng mengganti kerja program tersebut. Ikin membuat program tersebut hanya menampilkan hasil perkalian baris ganjil jika pertambahan  parameter bernilai genap, dan hanya menampilkan baris genap jika pertambahan parameter bernilai ganjil. Kemudian dia juga membuat program tersebut menampilkan kata “miau” ketika nilai baris dan nilai kolom sama. Terakhir, Ikin mengubah nama fungsi program tersebut menjadi tabel_perkalian_nggak_jelas. 

Ketentuan Tabel Perkalian
Ada dalam cerita diatas.

Dan ada dalam penjelasan parameter di bawah.

Penjelasan Parameter:
Ada 2 parameter untuk fungsi ini. Kedua parameter tersebut harus berupa bilangan bulat positif dan kurang dari 25. Apabila input parameter tidak memenuhi kriteria, maka fungsi harus menampilkan pesan "TIDAK VALID”. Nama parameter harus sesuai dengan ketentuan.

Format : 

baris = Menentukan jumlah baris. 

kolom = Menentukan jumlah kolom per baris.

 
Catatan Tambahan:
Jangan lupa baca soal terlebih dahulu, baca dengan teliti, jika masih tidak jelas baru tanyakan pada asdos

Untuk melakukan print hasil dalam 1 baris dapat menggunakan parameter end.

Jawaban menggunakan print() dan fungsi tidak menghasilkan nilai return.

Perhatikan jarak spasi print antar variabel.

Tips: Gunakan perulangan dalam perulangan, try-except, dan banyak percabangan.

Goodluck!!! ^^

tabel_perkalian_nggak_jelas(10,10) 
result : 
miau 2 3 4 5 6 7 8 9 10
3 6 miau 12 15 18 21 24 27 30
5 10 15 20 miau 30 35 40 45 50
7 14 21 28 35 42 miau 56 63 70
9 18 27 36 45 54 63 72 miau 90
"""

def tabel_perkalian_nggak_jelas(baris, kolom):
    try:
        if baris > 0 and kolom > 0 and baris < 25 and kolom < 25:
            jenis = 0
            if (baris + kolom) % 2 == 0:
                jenis = 1
            for i in range (1,baris+1):
                for j in range (1, kolom+1):
                    hasil = i * j
                    if i == j:
                        hasil = "miau"
                    if jenis == 0 and i % 2 == 0:
                        if j == kolom:
                            print(hasil)
                        else:
                            print(hasil, end=" ")
                    elif jenis != 0 and i % 2 != 0:
                        if j == kolom:
                            print(hasil)
                        else:
                            print(hasil, end=" ")
        else:
            print("TIDAK VALID")
    except TypeError:
        print("TIDAK VALID")
    return 0


