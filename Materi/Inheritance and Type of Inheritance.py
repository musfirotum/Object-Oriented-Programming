#default
class Fish :
    def __init__(self,firstname, lastname= "Fish",
                skeleton ="bone", eyelids= False):
        self.firstname = firstname
        self.lastname = lastname
        self.skeleton = skeleton
        self.eyelids = eyelids
    def swim(self):
        print ("The fish is swiming")
    def swim_backwards(self):
        print ("The fish can swim backwards")

class Trout(Fish):
    pass

class Clownfish(Fish):
    def live_with_anemone(self):
        print ("The clownfish is coexisting with sea anemoene")

terry = Trout("Terry")
print (terry.firstname+""+terry.lastname)
print (terry.skeleton)
print (terry.eyelids)
terry.swim()
terry.swim_backwards()

terry1=Trout("TerryS", "SmallFish", "no bone", True)
print (terry1.firstname+""+terry.lastname)
print(terry1.skeleton)
print(terry1.eyelids)

#override
class Fish :
    def __init__(self,firstname, lastname= "Fish",
                skeleton ="bone", eyelids= False):
        self.firstname = firstname
        self.lastname = lastname
        self.skeleton = skeleton
        self.eyelids = eyelids
    def swim(self):
        print ("The fish is swiming")
    def swim_backwards(self):
        print ("The fish can swim backwards")
        
class Shark(Fish):
    def __init__(self,firstname, lastname= "Shark",
                skeleton ="cartilage", eyelids= True):
        self.firstname = firstname
        self.lastname = lastname
        self.skeleton = skeleton
        self.eyelids = eyelids
    def swim_backwards(self):
        print ("The shark can not swim backwards, but can sink backwards ")
hiu = Shark("hiu besar")
hiu.swim_backwards()

#super
class User :
    def __init__ (self,name):
        self.name= name 
    def printName (self):
        print("Name =" + self.name)

class Programer(User): #baca inheriten super
    def __init__ (self,name,lastname):
        self.lastname = lastname
        super().__init__(name)
    def printlastname (self):
        print ("Last name =" + self.lastname)
    def doPython (self):
        print ("Programing Python")

class Programer1 (User):
    pass #mengambil atribut dan method yang sama dengan parent class



x = Programer("nama","lastname")
x.printName()
x.printlastname()
x.doPython()

#multiple
class Murid:
    
    def __init__(self):
        self.nama = input("Nama: ")
        
    def display(self):
        print("Nama: ",self.nama)
   
class NilaiPelajaran:
 
    def __init__(self):
        print("Nilai Pelajaran")
        self.math = int(input("Math: "))
        self.biology = int(input("Biology: "))
   
    def display(self):
        print("Rata2 Nilai: ", (self.math + self.biology)/2 )
        


class student(Murid, NilaiPelajaran):
    def __init__(self):
        Murid.__init__(self)
        NilaiPelajaran.__init__(self)
        
    def result(self):
        Murid.display(self)
        NilaiPelajaran.display(self)
        

stu1 = student()
stu2 = student()

stu1.result()
stu2.result()
