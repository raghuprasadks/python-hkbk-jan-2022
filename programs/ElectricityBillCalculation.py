'''
Electricity Bill calculation
'''
def calculateEBill(units):
    billamount=0
    if(units<=100):
        billamount = units*1
    elif (units>100 and units<=200):
        billamount= 100*1 + (units-100)*2
    elif(units>200 and units<=300):
        billamount=100 *1 + 100*2 +(units-200)*3
    else:
        billamount = 100 * 1 + 100 * 2 + 100*3 + (units - 300) * 4
    print("You have consumed ",units," your bill is ",billamount)

unitsconsumed = int(input("enter units consumed"))
calculateEBill(unitsconsumed)

