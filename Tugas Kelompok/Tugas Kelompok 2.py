#tugas 2 kelas A dan B
print ("Kelas 3 A")
print()

import datetime
waktu = datetime.datetime.now()
tahun = waktu.year

class Mhs :
    def __init__ (self,nama,npm):
        self.nama = nama
        self.npm = str(npm)
    def semester (self):
        waktu = datetime.datetime.now()
        nim = self.npm
        masuk = int(nim[0:2])
        mm = int(waktu.month)
        yy = int(waktu.year)
        if mm >= 8:
            sem = ((yy-2000) - masuk)*2+1
        elif mm < 8:
            sem = ((yy-2000)  - masuk)*2
        #ouput
        print('NIM:',self.npm)
        print("Semester:",sem)
    def tampilkan (self):
        print ("Nama saya adalah", self.nama)

maba = Mhs("fira",170411100051)
maba.tampilkan()
maba.semester()
print()
maba1 = Mhs("bagus",140411100051)
maba1.tampilkan()
maba1.semester()
print()
maba2 = Mhs("halimau jelek",180411100051)
maba2.tampilkan()
maba2.semester()


print ("Kelas 3 B")
print()
print ("Tugas 2 Kelompok PBO 3B")
print ("1. Bagus Fajariyanto  (170411100045)")
print ("2. Musfirotummamlu'ah (170411100051)")
print ()
print ("Kelas 3B")
print ()
import datetime
waktu = datetime.datetime.now()
class Pegawai:
    def __init__(self,no,nama,tahun,bulan,tanggal):
        self.nomor = no
        self.nama = nama
        self.thn = tahun
        self.bln = bulan
        self.tgl = tanggal
    def umurnow(self):
        th = waktu.year
        umur = th - self.thn
        return umur
    def lahirnya(self):
        return ("{}-{}-{}".format(self.tgl,self.bln,self.thn))

n = int(input("Jumlah Pegawai = "))
data = []
for i in range(n):
    nip = int(input("Masukkan Nomor Induk Pegawai = "))
    nama = str(input("Masukkan Nama = "))
    tahun = int(input("Masukkan Tahun lahir(yyyy) = "))
    bulan = int(input("Masukkan Bulan lahir(mm) = "))
    tanggal = int(input("Masukkan Tanggal lahir(dd)= "))  
    peg = Pegawai(nip,nama,tahun,bulan,tanggal)
    umur = peg.umurnow()
    lahir = peg.lahirnya()
    data1 = ["Nomer Induk Pegawai",nip,"\n","  Atas nama",nama,"\n","  Lahir pada tanggal",lahir,"\n","  Sekarang berumur %d tahun"%umur]
    data += [data1]
    print('Data berhasil di tambahkan')
    print()

print("--Daftar Pegawai--".center(45))
for i in range(len(data)):
    print("%d."%(i+1),end=" ")
    for j in range(len(data[i])):
        print(data[i][j],end=" ")
