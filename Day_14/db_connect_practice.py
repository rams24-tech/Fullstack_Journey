import psycopg2

class ExpenseTracker():
    def __init__(self):
        self.connection=psycopg2.connect(
            host="localhost",
            database="expense_tracker",
            user="postgres" ,
            password="Ramadevi@1984"
        )
        self.cursor=self.connection.cursor()
        print("Connected to database successfully!")

    def add_expense(self):
        desc=input("enter the description:")
        amt=float(input("Enter the amount"))
        self.cursor.execute("INSERT INTO expenses (description,amount) values (%s,%s);",(desc,amt))    
        self.connection.commit()
        print("Expense added!")

tracker=ExpenseTracker()
tracker.add_expense()