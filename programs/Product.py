'''
Product
'''

class Product():

    def __init__(self,code,name,desc,manu,price):
        self.code = code
        self.name = name
        self.desc = desc
        self.manu=manu
        self.price = price

    def info(self):
        return "Code : ",self.code ," Name : ",self.name," Description ",self.desc


prod1 = Product(1,"mobile 8 inch","RAM 8GB ","Nokia",25000)
prod2 = Product(2,"TV 56 inch","smart tv ","Sony",65000)

'''
product list
'''
productlist = []
productlist.append(prod1)
productlist.append(prod2)
'''
Product info
'''
for i in productlist:
    print(i.info())

'''
Sum of product price
'''
total = 0
for i in productlist:
    total = total +i.price
print("product price ",total)


