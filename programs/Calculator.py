'''
Calculator
'''
'''
def addition(num1,num2):
    result = num1 + num2
    print("Sum of  ",num1," and ",num2 ," is ",result)
num1=100
num2=200
addition(num1,num2)
'''
def addition(num1,num2):
    result = num1 + num2
    return result
def subtraction(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def division(num1,num2):
    return num1/num2
oper = input("Enter the operation +,-,*,/")
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
result = 0
if(oper=='+'):
    result = addition(num1,num2)
elif (oper=='-'):
    result = subtraction(num1,num2)
elif (oper=='*'):
    result = multiply(num1,num2)
elif (oper=='/'):
    result = division(num1,num2)
else:
    print("invalid operation")
print("result of ",num1, " ",oper,num2," is ",result)













