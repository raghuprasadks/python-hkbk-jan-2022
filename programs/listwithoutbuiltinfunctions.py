'''
List - without built-in functions
'''
marks = [20,19,16,22,6]
total = 0
maximum = 0
minimum = marks[0]
counter = 0
for i in marks:
    total = total + i
    if(i>maximum):
        maximum = i
    if(i<minimum):
        minimum=i
    counter = counter +1

print("total is ",total)
print("maximum is ",maximum)
print("minimum is ",minimum)
print("counter is ",counter)
avg=total/counter
print("Average is ",avg)