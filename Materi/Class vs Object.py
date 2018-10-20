#nomer 1
class Kubus : #keyword class diikuti dengan nama class yang diinginkan dan lebih baik diawali dengan huruf kapital.
    def __init__(self,s): #constructor menggunakan method bawaan dari python yg brnama init. method __init__() adalah metode konstruktor, yaitu metode khusus untuk menginisialisasi object dr class tsb
        self.sisi = s
    def tampilkansisi(self): #Setiap method harus memiliki parameter self yang artinya method tersebut dimiliki dan terdaftar ke class tersebut untuk membedakan dari method atau fungsi yang ada di luar class
        print (self.sisi)
    def luas (self):
        print ("Luas =", self.sisi**2)
    def volume (self):
        print("Volume =", self.sisi**3)
    def lp(self):
        print ("LP =", (self.sisi**2)*6)
        
Kubus1 = Kubus (4)
Kubus1.tampilkansisi()#mengakses object menggunakan operator titik
Kubus1.luas()

Kubus2 = Kubus (4)
Kubus2.tampilkansisi()
Kubus2.volume()

Kubus2 = Kubus (4)
Kubus2.tampilkansisi()
Kubus2.lp()

#nomer 2
class Mahasiswa :
    def __init__(self,npm,nama,ipk):
        self.n = npm
        self.na=nama
        self.i=ipk
    def tampilkan(self):
        print ("Mahasiswa dengan npm",self.n,",atas nama",self.na,"dengan ipk =",self.i)
    def kategori(self):
        ipk = self.i
        if ipk >=3.5 :
            print ("IPK =", ipk, "cumloud")
        elif ipk >3 and ipk<3.5 :
            print ("IPK=", ipk, "sagat memuaskan")
        elif ipk > 2.5 and ipk<=3:
            print ("IPK", ipk, "memuaskan")
        else :
            print ("IPK", ipk, "cukup")

m1= Mahasiswa("170411100051","Musfirotummamlu'ah", 4) #instansiasi Object(membuat object dari sebuah kelas), argumen sesuai dengan fungsi __init__() pada saat kita mendefinisikannya
m1.tampilkan()
m1.kategori()

#nomer 3
class Nasabah:
    def __init__(self,NoNasabah,Nama,NoRek,Saldo):
        self.nn= NoNasabah
        self.n=Nama
        self.nr=NoRek
        self.s = Saldo
    def tampilkan (self):
        print("Nasabah dengan nomer :", self.nn, "atas nama", self.n, "dengan no rekening", self.nr, "dan saldo Rp", self.s)
    def saldo(self):
        return self.s
    def norek(self):
        return self.nr
class Rekening :
    def __init__(self,Saldo,NoRek):
        self.s = Saldo
        self.nr = NoRek
    def ceksaldo (self):
        print("Saldo Anda :", self.s)
    def setoruang (self,setor):
        self.s += setor
        print("Anda Menambah", setor)
        print("saldo anda Rp", self.s)
    def ambiluang (self,ambil):
        self.s -=ambil
        print("Anda Mengambil ", ambil)
        print ("Saldo anda", self.s)
        
n1 = Nasabah ("1207", "fira", "1376986543", 300000)
n1.tampilkan()
norek = n1.norek()
sal = n1.saldo()
reken = Rekening(sal,norek)
n = int(input("Masukkan Uang yang anda setor = "))
reken.setoruang(n)
ambil = int(input("Masukkan nominal uang yang anda ambil = "))
reken.ambiluang(ambil)
reken.ceksaldo()

#nomer 4
class Pegawai :
    def __init__(self,n,j,g):
        self.nama=n
        self.jabatan = j
        self.gaji = g
    def tampilan(self):
        print(self.nama,",",self.jabatan,"dan",self.gaji)
p1 = Pegawai("adi", "penata muda", 5000)
p1.tampilan()
