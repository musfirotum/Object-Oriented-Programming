import datetime
waktu = datetime.datetime.now()
class Orang :
    def __init__(self, nama, tanggall, bulanl, tahunl,alamat):
        self.nama = nama
        self.tanggall = tanggall
        self.bulanl = bulanl
        self.tahunl= tahunl
        self.alamat = alamat
        self.umur = 0
    def perkenalkan(self):
        print ("Hello saya", self.nama, "\nSaya lahir pada", self.tanggall, self.bulanl, self.tahunl, "\nAlamat saya", self.alamat)
    def umur_skr(self):
        tahunskr = waktu.year
        self.umur = tahunskr - self.tahunl
    def prediksi_umur(self):
        tgl = int(input("Masukkan tanggal di masa depan untuk memprediksi umur anda (e.g 15): :"))
        bln = int(input("Masukkan bulan di masa depan untuk memprediksi umur anda (e.g 7): :"))
        th = int(input("Masukkan tahun di masa depan untuk memprediksi umur anda: (e.g 2020) :"))
        preumur = th - self.tahunl
        if bln > 0 :
            if bln >= self.bulanl :
                a = bln - self.bulanl
                print ("Umur anda pada tahun", th, "adalah", preumur, "tahun", a,"bulan"  )
            elif bln < self.bulanl :
                a = self.bulanl - bln
                b = 12 - a
                print("Umur anda pada tahun", th, "adalah", preumur-1, "tahun", b ,"bulan")
class Mhs (Orang):
    def __init__(self,nama,tanggall, bulanl, tahunl,alamat,jenjang, jurusan, perguruant, thlulus,ipk):
        Orang.__init__(self,nama,tanggall, bulanl, tahunl,alamat)        
        self.jenjang = jenjang
        self.jurusan = jurusan
        self.perguruant = perguruant
        self.thlulus = thlulus
        self.ipk = ipk
    def atribut (self):
        print ("Hello saya", self.nama, "\nSaya lahir pada", self.tanggall, self.bulanl, self.tahunl, "\nAlamat saya", self.alamat, "\nJenjang pendidikan", self.jenjang, "\nJurusan", self.jurusan, "\nPerguruan tinggi", self.perguruant, "\nTahun lulus", self.thlulus, "\nIPK", self.ipk)
    
    
orang = Orang ("fira", 12 , 5, 1999, "Pondok Halim 2 blok D2/03")
orang.perkenalkan()
orang.umur_skr()
orang.prediksi_umur()
print()
mhs = Mhs ("bagus", 17 , 8, 1999, "Jl. Rajawali", "S1", "Teknik Informatika", "Universitas Trunojoyo", 2020, 3.8)
mhs.atribut()
