#nomer 1
class Lingkaran :
    def __init__ (self,r) :
        self.r = r
    def tampilkanjari2 (self):
        print ("Jari jari : ", self.r)
    def luaspermukaan (self):
        print ("Luas permukaan lingkaran :",  3.14*self.r**2)
    def keliling (self):
        print ("Keliling lingkaran :",2*3.14*self.r)
class Tabung (Lingkaran):
    def __init__ (self,r,tinggi):
        self.t = tinggi
        Lingkaran.__init__(self,r)
    def luaspermukaan (self):
        print("Luas permukaan tabung :", 2*3.14*self.r*(self.t+self.r))

l1 = Lingkaran (4)
l1.tampilkanjari2()
l1.luaspermukaan()
l1.keliling()

t1= Tabung(2,3)
t1.tampilkanjari2()
t1.luaspermukaan()
print()
print()
#nomer 2
class Pecahan :
    def __init__(self, pembilang, penyebut):
        self.pem = pembilang
        self.pen = penyebut
        
    def Penyederhanaan (self):
        faktorpem = []
        for i in range(1, self.pem+1):
            if self.pem % i == 0 :
                faktorpem.append(i)
                
        faktorpen = []
        for i in range(1,self.pen+1):
            if self.pen % i == 0 :
                faktorpen.append(i)
                
        faktorsama = []
        for i in faktorpem :
            if i in faktorpen :
                faktorsama.append(i)
        fpb = max(faktorsama)
        pem = self.pem / fpb
        pen = self.pen / fpb
        print ("Pecahan sederhana dari :", self.pem, "/", self.pen, "adalah", int(pem),"/", int(pen))
a = Pecahan (20, 100)
a.Penyederhanaan()
print()
print()
#nomer3
class Pegawai :
    def __init__ (self, nama, idpegawai):
        self.nama = nama
        self.id = idpegawai
    def tampilkanpeg (self):
        print (" Nama pegawai :", self.nama,"\n id pegawai :", self.id)
class Toko :
    def __init__(self,namatoko,lokasi):
        self.namatoko = namatoko
        self.lokasi = lokasi
    def tampilkantoko(self) :
        print(" Nama toko :", self.namatoko, "\n Lokasi kerja :", self.lokasi)
        
class Penempatan (Pegawai,Toko):
    def __init__ (self,nama,idpegawai,namatoko,lokasi):
        Pegawai.__init__(self,nama,idpegawai)
        Toko.__init__(self,namatoko,lokasi)
    def tampil(self):
        Pegawai.tampilkanpeg(self)
        Toko.tampilkantoko(self)

p1 = Penempatan("fira", 120599, "Cendana store", "Jalan Pahlawan 10A, Bangkalan")   
p1.tampil()

print()
print()
#nomer4
class Mahasiswa:
    def __init__ (self, nama, npm):
        self.nama = nama
        self.npm = npm
    def tampilkanmhs(self):
        print("Nama mahasiswa :", self.nama, "\nNPM :", self.npm)
class Matakuliah :
    def __init__ (self):
        self.kode = [301,302,303,304,305,306]
        self.namamk = ["Matematika Diskrit","Sistem Basis Data","Pemrograman Berorientasi Objek","Sistem Operasi","Rekayasa Multimedia","Pemrograman Desktop"]
        
    def tampilkanmk(self):
        print("-".center(80,"-"))
        print("daftar kode dan nama matakuliah".center(80).upper())
        for i in range(6):
            print("{} - {}".format(self.kode[i],self.namamk[i]))
        print("-".center(80,"-"))        
        
class Pengambilanmk (Mahasiswa,Matakuliah):
    def __init__(self,nama,npm):
        self.nilai=[]
        self.data = []
        self.ips = 0
        Mahasiswa.__init__(self,nama,npm)
        Matakuliah.__init__(self)
        
    def ambil (self):
        tambah = int (input ("Masukkan jumlah matakuliah yang ingin anda ambil :"))
        for i in range(tambah):
            i+=1
            ambil = int(input("Masukkan kode matakuliah yang ingin diambil:"))
            self.data.append(ambil)
        print ("Kode matakuliah yang diambil :", self.data)
        for i in range (tambah):
            i+=1
            angka=int (input("Masukkan nilai matakuliah ke %d:" %i))
            self.nilai.append(angka)
            self.ips += angka
        self.ips /= i
      
    def tampil(self):
        Matakuliah.tampilkanmk(self)
                
    def output (self):
        print("matakuliah yang berhasil diambil".center(80).upper())
        Mahasiswa.tampilkanmhs(self)
        for i in (self.data):
            if i == 301 :
                print("TIK301 - Matematika Diskrit")
            elif i == 302 :
                print("TIK302 - Sistem Basis Data")
            elif i == 303 :
                print("TIK303 - Pemrograman Berorientasi Objek")
            elif i == 304 :
                print("TIK304 - Sistem Operasi")
            elif i == 305 :
                print("TIK305 - Rekayasa Multimedia")
            elif i == 306 :
                print("TIK306 - Pemrograman Desktop")
        print ("Nilai matakuliah :", self.nilai)
        print ("IPS :", self.ips)

            
        

m= Pengambilanmk("fira",170411100051)
m.tampil()
m.ambil()
m.output()  
