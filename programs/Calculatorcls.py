'''
Class and object
'''
class Calculator():
    #attributes/properties
    num1=1
    num2=1
    '''
    add method
    '''
    def add(self):
        result = self.num1+self.num2
        return result
    def subtract(self):
        return self.num1-self.num2
'''
mycalci - object
'''
mycalci = Calculator()
mycalci.num1=100
mycalci.num2=200
res=mycalci.add()
print('result is addition is ',res)
res=mycalci.subtract()
print('result is subtraction is ',res)

mycalci2 = Calculator()
mycalci2.num1=200
mycalci2.num2=300
res=mycalci2.add()
print('result is addition from mycalci2 ',res)




