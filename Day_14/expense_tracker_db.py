import psycopg2


class ExpenseTracker():
    def __init__(self):
        self.connection = psycopg2.connect(
            host="localhost",
            database="expense_tracker",
            user="postgres",
            password="Ramadevi@1984"
        )
        self.cursor = self.connection.cursor()
        print("Connected to database successfully!")

    def add_expense(self):
        description = input("Enter description: ")
        amount = float(input("Enter amount: "))
        self.cursor.execute("INSERT INTO expenses (description, amount) VALUES (%s, %s);", (description, amount))
        self.connection.commit()
        print("Expense added!")
 

    def view_all(self):
        self.cursor.execute("SELECT * FROM expenses")
        rows = self.cursor.fetchall()
        for row in rows:
            print(f"ID: {row[0]} | {row[1]} | ${row[2]} | {row[3]}")


    def view_total(self):
        self.cursor.execute("SELECT SUM(amount) FROM expenses")
        result = self.cursor.fetchone()
        print(f"Total: ${result[0]}")


    def close(self): 
        self.cursor.close()
        self.connection.close()        
tracker = ExpenseTracker()

while True:
    print("\n1. Add expense")
    print("2. View all")
    print("3. View total")
    print("4. Quit")
    
    choice = input("Choose: ")
    
    if choice == "1":
        tracker.add_expense()
    elif choice == "2":
        tracker.view_all()
    elif choice == "3":
        tracker.view_total()
    elif choice == "4":
        tracker.close()
        print("Goodbye!")
        break
        
        
        
        
        
        
        
        
        
        
        
   
