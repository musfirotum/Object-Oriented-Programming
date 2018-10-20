#contoh 1
def add(datatype, *args):

    if datatype =='int':
        answer = 0

    if datatype =='str':
        answer =''

    for x in args:

        answer = answer + x

    print(answer)

# Integer
add('int', 5, 6)

# String
add('str', 'Hi ', 'Geeks')

#contoh 2

class Human:
    def sayHello(self, name=None):
        if name is not None:
            print('Hello ' + name)
        else:
            print('Hello ')
# Create instance
obj = Human()

# Call the method
obj.sayHello()

# Call the method with a parameter
obj.sayHello('Guido')

#contoh 3

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    #def __str__(self):
    #   return "({0},{1})".format(self.x,self.y)
    def __str__(self):
        return "Point object is at: (" + str(self.x) + ", " + str(self.y) + ")"
    def __sub__(self,other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x,y)
p1 = Point(2,3)
p2 = Point(-1,2)
print(p1 - p2) # bisa ditulis dengan p1.__add__(p2)

#contoh 4
class Fraction:
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom
        
    #def show(self):
    #    print(self.num,"/",self.den)
    
    def __str__(self):
        return str(self.num)+"/"+str(self.den)
        f=Fration(2,4)
#Show(f)
#print(f)
    def __add__(self,otherfraction):

        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum,newden)
f1 = Fraction(1,4)
f2 = Fraction(1,2)
print(f1+f2)

