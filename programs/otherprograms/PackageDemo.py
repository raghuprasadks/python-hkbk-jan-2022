import Calculator as calci
from Calculator import multiply

print("Calculator - add ")
num1 = int(input("Enter a number 1"))
num2 = int(input("Enter a number 2"))
result = calci.add(num1,num2)
print("res {} + {} is {}".format(num1,num2,result))

print("Calculator - multiplication demo")

result = multiply(4,5)
print("Calculator - multiply ",result)