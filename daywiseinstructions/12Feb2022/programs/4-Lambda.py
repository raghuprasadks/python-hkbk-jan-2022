'''
Lambda - annonymous fuctions
'''
'''
def add(num1,num2):
    return num1 + num2

print ("sum is ",add(100,200))
'''
'''
total = lambda n1,n2: n1+n2
print("Lambda -total ",total(10,20))
'''
'''
x = lambda a : a + 10
print('lamdba 2 - adding a value' ,x(5))
'''
'''
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
'''
'''
#Filter
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
even_list = []
for i in my_list:
    if (i%2==0):
        even_list.append(i)
print("Even list ",even_list)
'''
'''
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

# another way of creating list using list constructor
anotherway=list([20,30,50,40])
print("Another way of creating a list",anotherway)
new_list = list(filter(lambda x: (x % 2==0) , my_list))
print("filtered list " ,new_list)
'''
'''
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2 , my_list))
print("After mapping ",new_list)
'''
'''
#functools is a package/module reduce is a function
from functools import reduce
li = [5, 8, 10, 20, 50, 100]
print("sum of li ",sum(li))

sum = reduce((lambda x, y: x + y), li)
print (sum)
avg = sum/len(li)
print('average ',avg)
'''