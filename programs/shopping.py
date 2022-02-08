purchaseamt = float(input("Enter purchase amount"))
discount=0
netamount=0
if (purchaseamt <10000):
    discount = 0.05
elif (purchaseamt >=10000 and purchaseamt <20000):
    discount = 0.1
elif (purchaseamt >=20000 and purchaseamt <30000):
    discount = 0.15
else:
    discount = 0.2
discount = purchaseamt*discount
netamount=purchaseamt-discount
print("Netamout to be paid  ",netamount)
print ("discount ",discount)

