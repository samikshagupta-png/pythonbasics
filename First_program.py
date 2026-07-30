#encapsulation
class account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account = acc

    def debit(self,amount):
        self.balance-=amount
        print("rs.",amount,"was debited")
        print("total balance",self.get_balance())
    def credit(self,amount):
        self.balance+=amount
        print("rs.",amount,"was credited")
        print("total balance",self.get_balance())

    def get_balance(self):
        return self.balance


acc1 =account(45648,785)
print(acc1.account)
print(acc1.balance)
acc1.debit(1000)
acc1.debit(500)

class car:
    color = "black"
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped")
class toyotacar(car):
    def __init__(self,name):
        self.name = name
car1 = toyotacar("fortuner")
car2 = toyotacar("pri")
print(car1.color)

class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class c(A,B) :
    varc = "welcome to class C"
c1=c()
print(c1.varc)
print(c1.varB)
print(c1.varA)
class students:
    def __init__(self,phy,chem,math):

        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy + self.chem +self.math)/3) + "%"
    def calcpercentage(self):
        self.percentage = str((self.phy + self.chem +self.math)/3) + "%"
stu1= students(98,97,99)
print(stu1.percentage)


        
        



        

        