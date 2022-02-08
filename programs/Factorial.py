'''
Program to find the factorial of a given number
'''

def factorial(num):
    fact=1
    for i in range (1,num+1):
        fact = fact*i
    print("factorial of ",num, " is ",fact)

fact= int(input("Enter a number to find its factorial"))
factorial(fact)