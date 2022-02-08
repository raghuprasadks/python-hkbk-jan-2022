'''
Dictionary
key should be unique
'''
'''
students={100:"Abdul",101:"Chandru",102:"Joseph",100:"Rahman"}
print("student dictionary ",students)
students[104]="Raghu"
students[105]="Gagan"
students[100]="Abdul Khan"
del students[100]
print("updated dictionary ",students)
'''
'''
Dynamic dictionary
aadhardicts={aadhar1:name1,aadhar2:name2}
'''
'''
fmlymembers = int(input("Enter number of family members"))
aadhardicts={}
for i in range(fmlymembers):
    aadharnum=int(input("Enter Aadhar number"))
    name = input("Enter name")
    aadhardicts[aadharnum]=name

print("aadhar dictionary")
print(aadhardicts)
'''
'''
display only keys
'''
'''
print("keys ",aadhardicts.keys())
print("values ",aadhardicts.values())

for k,v in aadhardicts.items():
    print("key = ",k," value = ",v)
'''
'''
vaccinationdict{"statename":[1stdose,2nddosecount,boostercount]}
'''
'''
'''
vaccinationdict={"Karnataka ":[10000,5000,1000],"Tamil Nadu ":[20000,8000,1000]}
print("vaccinationdict : ",vaccinationdict)

for k,v in vaccinationdict.items():
    print("key = ",k, " value = ",v)

'''
in and not in
'''
print("is kelara in the dictionary " ,"kerala" in vaccinationdict)
print("is karnataka in the dictionary " ,"karnataka" in vaccinationdict)

