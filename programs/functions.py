'''
functions
'''

def greet():
    print("Welcome to python programming")

greet()
greet()

def greet(name):
    print(name, "Welcome to python programming")

name = input("enter your name")
greet(name)
greet("Rahman")

def evenOrOdd(num):
    if(num %2 ==0):
        print(num, "is even")
    else:
        print(num, "is odd")

evenOrOdd(20)

