'''
Account class with constructor
deposit()
withdraw()
openaccount()
checkbalance()
'''

class Account():
    '''
    name,email - local variable
    self.name - instance variable
    __init__ - constructor
    '''
    def __init__(self,name,email,address,mobile,idproof):
        self.name = name
        self.email = email
        self.address = address
        self.mobile = mobile
        self.idproof = idproof
        self.accountno=100
        self.balance=0


    def deposit(self,accountno,amttodeposit):
        self.balance = self.balance + amttodeposit
        return self.balance

    def withdraw(self, accountno, amttowithdraw):
        self.balance = self.balance - amttowithdraw
        return self.balance

    def checkBalance(self,accountno):
        return self.balance

act1 = Account('raghu','raghu@gmail.com','jakkuru,Bengaluru',9845547471,'Aadhar -9999')
#actno =act1.openAccount('raghu','raghu@gmail.com','jakkuru,Bengaluru',9845547471,'Aadhar -9999')
act1.accountno
bal =act1.deposit(actno,10000)
print('Balance after deposit of 10 k is ',bal)
bal =act1.deposit(actno,20000)
print('Balance after deposit of 20 k is ',bal)
bal =act1.withdraw(actno,5000)
print('Balance after withdraw of 5 k is ',bal)
bal =act1.checkBalance(actno)
print('Balance checkbalance ',bal)

