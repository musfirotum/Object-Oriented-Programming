#contoh 1
class Mahasiswa :
    __name = ""
    def __init__ (self):
        self.__name = "Musfirotum"
        
    def printname (self):
        print ('Name :'+str(self.__name))
        
    def setName (self,nama):
        self.__name = nama

mhs = Mahasiswa()
mhs.printname()
mhs.setName("Musfirotum")
#mhs.printname()

#contoh 2

class Mahasiswa :
    def __init__ (self):
        self.__updateName = "fira"
        
    def printname (self):
        print ('Updating name : '+str(self.__updateName))
        
    def __updateName(self):
        print ('Updating name : '+str(self.__updateName))

mhs = Mahasiswa()
mhs.printname()
mhs._Mahasiswa__updateName

#contoh 3
class A(object):
	# public method
	def myPublicMethod(self):
		return "This is a public method"

	# private method with single _underscore
	def _myPrivateMethod(self):
		return "This is a private method"

	# private metod with double __undersore
	def __myAnotherPrivateMethod(self):
		return "This is another private Method"


obj = A()
# We can access the public method which is cool !!!
print(obj.myPublicMethod())   #Output : This is a public method

# Note that we can also access the private method from outside
print(obj._myPrivateMethod()) #Output : This is a private method

# However, You can still call the double underscore method
# by appending the _class name before method name
print(obj._A__myAnotherPrivateMethod()) #Output:This is another private Method
