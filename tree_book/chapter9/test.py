class FirstClass(object):
    def setdata(self,value):
        self.data = value
    def display(self):
        print(self.data)

class SecondClass(FirstClass):
    def __init__(self,value):
        self.data = value
    def __add__(self,other):
        return SecondClass(self.data + other)
    def __str__(self):
        return 'hello：%s'%self.data


y = SecondClass('adc') 
y.display() #adc
print(y)    #hello：adc
b = y + 'xyz'   
b.display()     #adcxyz


