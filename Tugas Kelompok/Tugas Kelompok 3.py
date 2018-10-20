#User
class User:
    def __init__(self,firstname):
        self.name = firstname
        
    def printName(self):
        print("First Name =",self.name)

class Programmer(User):
    def __init__(self,firstname,lastname):
        super().__init__(firstname)
        self.lastname = lastname
        
    def printLastName(self):
        print("Last Name =",self.lastname)

awal = str(input("Nama Depan = "))
belakang = str(input("Nama Belakang = "))
print()
print("---Hasil----")
x = Programmer(awal,belakang)
x.printName()
x.printLastName()
print("Nama Lengkap: {} {}".format(x.name,x.lastname))
print ()

#Mahasiswa, dosen, karyawan
import datetime
class Orang:
    def __init__(self,name):
        self.name = name
        
    def printName(self):
        print("Nama =",self.name)

class Mahasiswa(Orang):
    def __init__(self,name,npm):
        self.npm = str(npm)
        super().__init__(name)
        
    def semester(self):
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
        
class Pegawai(Orang):
    def __init__(self,name,nip):
        self.nip = nip
        super().__init__(name)
        
    def data(self):
        print("Nama: {} ; NIP: {}".format(self.name,self.nip))
        
class Dosen(Pegawai):
    def __init__(self,name,nip,nidn):
        super().__init__(name,nip)
        self.nidn = nidn
    
    def output(self):
        print("Nama: {} ; NIP: {} ; NIDN: {}".format(self.name,self.nip,self.nidn))
        
class Karyawan(Pegawai):
    pass


mhs = Mahasiswa("Ikhwan",170411100045)
mhs.printName()
mhs.semester()
print()
dosen = Dosen("Bagus Fajariyanto",1412290834142,12345)
dosen.output()
print()
kar = Karyawan("Fiirraaa",128976986124)
kar.data()
print()
