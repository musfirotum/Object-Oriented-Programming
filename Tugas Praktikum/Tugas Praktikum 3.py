print("Nomer 1 - 3")
class KategoriBarang :
    def __init__ (self, kode, deskripsi):
        self.kode = kode
        self.deskripsi = deskripsi
    def tampil_kode (self):
        print ("Kode barang :", self.kode, "\nDeskripsi:", self.deskripsi)
    def tampil_kategori (self):
        a = int (input("Pilih kategori 1 atau 2:"))
        if a == 1 :
            print ("Kategori : Makanan")
        elif a ==2 :
            print ("Kategori : Pakaian")
            
class Barang (KategoriBarang):
    def __init__ (self,nama,harga,diskon,kode, deskripsi):
        KategoriBarang.__init__(self,kode, deskripsi)
        self.nama = nama
        self.harga = harga
        self.diskon = diskon
    def tampil_semua (self):
        raise NotImplementedError ("Subclass must implementent abstrack method")

class Makanan (Barang):
    def __init__(self, nama, harga, diskon, exdate, kode, deskripsi):
        Barang.__init__(self,nama, harga, diskon,kode, deskripsi)
        self.exdate = exdate
    def discount (self):
        dis = self.harga - self.diskon
        print("Diskon harga :", self.diskon, "\nTotal harga yang harus anda bayar:", dis)
    def tampil_semua(self):
        print ("Nama barang:", self.nama, "\nHarga:", self.harga, "\nExDate :", self.exdate)

class Pakaian (Barang):
    def __init__(self, nama, harga, diskon, ukuran,kode, deskripsi):
        Barang.__init__(self,nama, harga, diskon, kode, deskripsi)
        self.ukuran = ukuran
    def discount (self):
        dis = self.harga - self.diskon
        print("Diskon harga :", self.diskon, "\nTotal harga yang harus anda bayar:", dis)
    def tampil_semua(self):
        print ("Nama barang:", self.nama, "\nHarga:", self.harga, "\nUkuran :", self.ukuran)
        
print("=".center(80,"="))
print("1. kelas abstrak pemanggilan biasa".center(80).upper())
a = KategoriBarang(112, "Candy with less sugar")
a.tampil_kode()
a.tampil_kategori()
a1 = Makanan ("Candy", 30000, 2000, "12-12-2012", 1, "Candy with less sugar")
a1.tampil_semua()
a1.discount()
print()
b = KategoriBarang(221, "Product of Nevada")
b.tampil_kode()
b.tampil_kategori()
b1=Pakaian("Nevada", 300000, 20000, "L", "2","Product of Nevada" )
b1.tampil_semua()
b1.discount()
print("=".center(80,"="))

print("2. pemanggilan dengan function".center(80).upper())
def kode (KategoriBarang):
    KategoriBarang.tampil_kode()
def kategori(KategoriBarang):
    KategoriBarang.tampil_kategori()
def tamsemua(Barang):
    Barang.tampil_semua()
def dis (Barang):
    Barang.discount()
    
a = KategoriBarang(112, "Candy with less sugar")
a1 = Makanan ("Candy", 30000, 2000, "12-12-2012", 1, "Candy with less sugar")
b = KategoriBarang(221, "Product of Nevada")
b1=Pakaian("Nevada", 300000, 20000, "L", "2","Product of Nevada" )

kode(a)
kategori(a)
tamsemua(a1)
dis(a1)
print()
kode(b)
kategori(b)
tamsemua(b1)
dis(b1)
print("=".center(80,"="))

print("3. pemanggilan dengan method".center(80).upper())
a = KategoriBarang(112, "Candy with less sugar")
a1 = Makanan ("Candy", 30000, 2000, "12-12-2012", 1, "Candy with less sugar")
b = KategoriBarang(221, "Product of Nevada")
b1=Pakaian("Nevada", 300000, 20000, "L", "2","Product of Nevada" )

a.tampil_kode()
a.tampil_kategori()
a1.tampil_semua()
a1.discount()
print()
b.tampil_kode()
b.tampil_kategori()
b1.tampil_semua()
b1.discount()
print("=".center(80,"=")) 

class Makanan :
    def nama (self):
        nama = str(input("Nama makanan:"))
        return nama
    def harga (self):
        harga = int(input("Harga barang:"))
        return harga
    def diskon (self):
        diskon = int(input("Diskon :"))
        return diskon
    def total (self):
        a= Makanan.harga(self)
        b= Makanan.diskon(self)
        print("Total harga yang harus anda bayar", a-b)
    def exp (self):
        print ("ExDate : 12-12-2012")
class Pakaian :
    def nama (self):
        nama = str(input("Merk pakaian:"))
        return nama
    def harga (self):
        harga = int(input("Harga pakaian:"))
        return harga
    def diskon (self):
        diskon = int(input("Diskon :"))
        return diskon
    def total (self):
        a= Pakaian.harga(self)
        b= Pakaian.diskon(self)
        print("Total harga yang harus anda bayar", a-b)
    def ukuran (self):
        print ("Ukuran : L")
    
a = Makanan()
a.nama()
a.exp()
a.total()
print()
b = Pakaian()
b.nama()
b.ukuran()
b.total()
