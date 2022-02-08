"""
Operators
1. Arithmetic Operator
"""
num1 = 100
num2 = 200
result = num1+num2
print(num1," + ",num2, ' = ',result)
result = num2/num1
print(num2," / ",num1, ' / ',result)
num3=10
num4=3
result = num3%num4
print(num3," % ",num4, ' % ',result)
result = num3//num4
print(num3," // ",num4, ' // ',result)

"""
2. Comparision/Relational Operator
>,<,>=,<=,==,!=
"""
num1=300
num2=200
num3=200
print(" demo of > ",num1>num2)
result = num2==num3
print(" demo of == ",result)
result = num2!=num3
print(" demo of != ",result)
result = num2>=num3
print(" demo of >= ",result)

"""
3. Logical Operator
and , or ,not
"""

num1= 100
num2=75
num3=50

result = num1>num2 and num2>num3
print("demo of and - True ",result)
result = num1<num2 and num2>num3
print("demo of and - False",result)
result = not (num1>num2 and num2>num3)
print("demo of not",result)
sum = 100
sum = sum +10
print ("sum is ",sum)
sum += 20
#sum = sum +20
print (" updated sum is ",sum)




