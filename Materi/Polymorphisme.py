#abstrack class
class Pegawai :
    def __init__ (self,nama):
        self.nama = nama
    
    def gaji (self):
        raise NotImplementedError ("Subclass must implementent abstrack method")#ciri abstrak class
    
class Manajer(Pegawai):
    def __init__(self,nama,tunjangan):
        Pegawai.__init__(self,nama)
        self.tunjangan = tunjangan
    def gaji (self):
        gaji= int (input ("Masukkan nominal gaji anda:"))
        totalgaji = gaji + self.tunjangan
        print ("Total gaji keseluruhan : ",totalgaji)

class Programer(Pegawai):
    def __init__(self,nama,bonus):
        Pegawai.__init__(self,nama)
        self.bonus = bonus
    def gaji (self):
        gaji= int (input ("Masukkan nominal gaji anda:"))
        totalgaji = gaji + self.bonus
        print ("Total gaji keseluruhan : ",totalgaji)
p = Manajer("fira", 300000)
p.gaji()
print()
p2 = Programer ("tatitu", 6000000)
p2.gaji()

#polymorphism dg function
class Pegawai :
    def __init__ (self,nama):
        self.nama = nama
    
    def gaji (self):
        raise NotImplementedError ("Subclass must implementent abstrack method")#ciri abstrak class
    
class Manajer(Pegawai):
    def __init__(self,nama,tunjangan):
        Pegawai.__init__(self,nama)
        self.tunjangan = tunjangan
    def gaji (self):
        gaji= int (input ("Masukkan nominal gaji anda:"))
        totalgaji = gaji + self.tunjangan
        print ("Total gaji keseluruhan : ",totalgaji)

class Programer(Pegawai):
    def __init__(self,nama,bonus):
        Pegawai.__init__(self,nama)
        self.bonus = bonus
    def gaji (self):
        gaji= int (input ("Masukkan nominal gaji anda:"))
        totalgaji = gaji + self.bonus
        print ("Total gaji keseluruhan : ",totalgaji)

def gajinya (Pegawai):
    Pegawai.gaji()
p1 = Manajer("fira", 300000)
p2 = Programer("tata", 600000)

gajinya(p1)
gajinya(p2)

#polymorphism dengan method
class Pegawai :
    def __init__ (self,nama):
        self.nama = nama
    
    def gaji (self):
        raise NotImplementedError ("Subclass must implementent abstrack method")#ciri abstrak class
    
class Manajer(Pegawai):
    def __init__(self,nama,tunjangan):
        Pegawai.__init__(self,nama)
        self.tunjangan = tunjangan
    def gaji (self):
        gaji= int (input ("Masukkan nominal gaji anda:"))
        totalgaji = gaji + self.tunjangan
        print ("Total gaji keseluruhan : ",totalgaji)

class Programer(Pegawai):
    def __init__(self,nama,bonus):
        Pegawai.__init__(self,nama)
        self.bonus = bonus
    def gaji (self):
        gaji= int (input ("Masukkan nominal gaji anda:"))
        totalgaji = gaji + self.bonus
        print ("Total gaji keseluruhan : ",totalgaji)
        
p1 = Manajer("fira", 300000)
p2 = Programer("tata", 600000)

for pegawai in (p1,p2):
    pegawai.gaji()

#class manajer dan class progammer bukan inheritance
class Manajer ():
    def nama (self):
        nama = str (input ("Nama saya :"))
    def gaji (self):
        gaji= int (input ("Masukkan nominal gaji anda:"))
        return gaji
    def tunjangan (self):
        tunjangan= int (input ("Masukkan nominal tunjangan anda:"))
        return tunjangan
    def total(self):
        a=Manajer.gaji(self)
        b=Manajer.tunjangan(self)
        print ('Total gaji : ',a+b)
class Programer ():
    def nama (self):
        nama = str (input ("Nama saya :"))
    def gaji (self):
        gaji= int (input ("Masukkan nominal gaji anda:"))
        return gaji
    def bonus (self):
        bonus= int (input ("Masukkan nominal bonus anda:"))
        return bonus
    def total(self):
        a=Programer.gaji(self)
        b=Programer.bonus(self)
        print ('Total gaji : ',a+b)
                           
a=Manajer()
a.nama()
a.total()
print ()

b=Programer()
b.nama()
b.total()   

