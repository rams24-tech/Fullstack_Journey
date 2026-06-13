class BankAccount:
    def __init__(self,owner,Balance):
        self.owner=owner
        self.Balance=Balance

    def deposit(self,amount):
        self.Balance=self.Balance+amount
        print(f"Deposited {amount}.New Balance :{self.Balance}")

    def withdraw(self,amount):
        if amount>self.Balance:
            print("insufficient funds.")
        else:    
            self.Balance=self.Balance-amount
            print(f"Withdrew {amount}.New balance:{self.Balance}")

    def show_balance(self):
        print(f"Account owner: {self.owner} | Balance: {self.Balance}")    
                 
acc_1=BankAccount("Kasi",2500)
acc_2=BankAccount("Vinay",3000)                 

acc_1.deposit(200)
acc_1.show_balance()
acc_1.withdraw(500)
acc_1.show_balance()
acc_2.deposit(200)
acc_2.show_balance()
acc_2.withdraw(500)
acc_2.show_balance()
acc_2.withdraw(10000000)