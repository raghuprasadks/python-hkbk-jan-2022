'''
Exceptions
'''
'''
print("Exception scenario")
num=int(input("Enter a number"))
result = 100/num
print("result is ",result)
'''
'''
print("Handling exception")
try:
    num = int(input("Enter a number"))
    result = 100 / num
    print("result is ", result)
except:
    print("Exception occured")
print("After exception")
'''
'''
try:
    num = input("Enter a number")
    result = 100 / num
    print("result is ", result)
except Exception as e:
    print("Exception occured",e)
print("After exception")
'''
'''
print("Arry index out of bound exception")
import traceback
try:
    marks=[10,20,30,40]
    mymarks=marks[4]
    print("result is ", mymarks)
except IndexError:
    print("Index error has occured")
except:
    print("Exception occured",traceback.print_exc())
print("After exception")
'''
'''
print("Finally block")
try:
    name=''
    print("Length ", len(name))
except Exception as e:
    print ("Error has occured ",e)
finally:
    print("Finally is always executed ")
print("After error")
'''
'''
print("Custom exception or user defined exception")
class InvalidData(Exception):

    def __init__(self,error):
        self.error=error

    def __str__(self):
        return "Invalid data {}".format(self.error)

print("Throw custom error")
try:
    name=''
    print("Length ", len(name))
    if (len(name)<=1):
        raise InvalidData("Length should be greater than 1")
except Exception as e:
    print ("Error has occured ",e)
finally:
    print("Finally is always executed ")
print("After error")
'''



