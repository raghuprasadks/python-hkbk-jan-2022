'''
Sum of digits
'''
def SumOfDigits(num):
    numentered=num
    sum=0
    while(num>0):
        sum = sum + num%10
        num=num//10
    print("Sum of digits of ",numentered, " is ",sum)
num = int(input("Enter a number"))
SumOfDigits(num)