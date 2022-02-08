'''
Program to find a given number is prime or not
'''
#incorrect.. Does not work for all scenarios
def isPrime(num):
    for i in range(2,num):
        if (num%i==0):
            print(num,"is not a prime number")
            break
        else:
            print(num,"is a prime number")
            break

n=int(input("Enter a number to check it is prime or not"))
isPrime(n)


def isPrime(num):
    isPrimeNum = True
    for i in range(2,num):
        if(num%i==0):
            isPrimeNum=False
            break
    if(isPrimeNum==True):
        print(num,"is prime number")
    else:
        print(num,"is not prime number")

n=int(input("Enter a number to check it is prime or not"))
isPrime(n)