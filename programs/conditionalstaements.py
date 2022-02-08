'''
conditional statements
'''
age = 17

if (age >= 18):
    print("You are eligible to vote")
else:
    print("you are not eligible to vote")

'''
Display grade based on marks

marks - 90 to 100 - A+
marks - 80 to 90 - A
marks - 71 to 80 - B+
marks - 61 to 70 - B
other than above - c
'''
print("Display grade based on the marks")
marks = 80
if (marks >90 and marks <=100):
    print("A+")
elif (marks >80 and marks <=90):
    print("A")
elif (marks >70 and marks <=80):
    print("B+")
elif (marks >60 and marks <=70):
    print("B")
else:
    print("C")


