'''
List
marks = [30,40,70,90,90]
Built in functions
'''
marks = [30,40,70,90,99,23]
print("list length is ",len(marks))
print("sum of elements in the list ",sum(marks))
print("maximum value  ",max(marks))
print("minimum value  ",min(marks))
avg = sum(marks)/len(marks)
print("Average is ",avg)
marks.append(45)
print("After append ",marks)

'''
Dynamic list
'''
friends=[]
numoffriend= int(input("enter number of friends to invite"))
for i in range(numoffriend):
    name = input("Enter friend to invite")
    friends.append(name)
print("Friends list ",friends)

friendslist = ['Rahman','Swami','Joseph']

coronalist=[]
heading = ['State','Active','Recovered','Death','Total']
state1 = ['Karnataka',1000,8000,1000,10000]
state2 = ['Tamilnadu',2000,16000,2000,20000]
coronalist.append(heading)
coronalist.append(state1)
coronalist.append(state2)
print("Corona Dashboard")
print(coronalist)







