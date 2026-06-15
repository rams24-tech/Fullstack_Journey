class Expense:
    def __init__(self,description,amount):
        self.description=description
        self.amount=amount
        
    def __str__(self):
        return f"{self.description},{self.amount}"   
    
class ExpenseTracker():
    def __init__(self,filename):
        self.filename=filename  

    def add_expense(self):
        with open(self.filename, "a") as file:
            description = input("Enter description: ")
            amount = input("Enter amount: ")
            expense = Expense(description, amount)
            file.write(str(expense) + "\n")
        print("Expense added!")    
    
    def view_all(self):
        with open(self.filename, "r") as file:
            print("All expenses:")
            for line in file:
                parts = line.strip().split(",")
                print(f"{parts[0]} - ${parts[1]}")
            

    def view_total(self):
        total=0
        with open(self.filename, "r") as file:   
            for line in file:
                parts=line.strip().split(",")
                amount=float(parts[1]) 
                total=total+amount
            print(f"Total: {total}")        

def menu():
    print("Expense Tracker")
    print("_______________")
    print("1.Add expense")
    print("2.View all expenses")
    print("3.View total")
    print("4. Quit")

tracker = ExpenseTracker("expenses.txt")
i=0
while i==0:
    menu()
    x=int(input("Choose an option: "+"\n"))
    if x==1:
        tracker.add_expense()
    elif x==2:
        tracker.view_all()
    elif x==3:
        tracker.view_total()
    elif x==4:
        print("Goodbye!!")
        i=i+1    








