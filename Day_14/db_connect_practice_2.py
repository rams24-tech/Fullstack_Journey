import psycopg2

class ExpenseManager():
    def __init__(self):
        self.connection=psycopg2.connect(
            host="localhost",
            database="expense_tracker" ,
            user="postgres" ,
            password="Ramadevi@1984"
        )
        self.cursor =self.connection.cursor()
        print("Connection Established")

    def add_expense(self):
        desc=input("Enter the Description:")  
        amount=float(input("Enter the amount:"))
        self.cursor.execute("INSERT INTO expenses (description,amount) VALUES (%s,%s);" ,(desc,amount))  
        self.connection.commit()
        print("Expense Added!")

    def view_all(self):
        self.cursor.execute("SELECT * FROM expenses")
        rows=self.cursor.fetchall()
        for row in rows:
            print(f"ID:{row[0]} | DESCRIPTION:{row[1]} | AMOUNT:{row[2]} | DATE: {row[3]}")

    def view_total(self):
        self.cursor.execute("SELECT sum(amount) FROM expenses")
        result=self.cursor.fetchone()
        print(f"Total: ${result[0]}")

    def close(self):
        self.cursor.close()
        self.connection.close()
        print("Connection closed!")  

manager = ExpenseManager()
manager.add_expense()
manager.view_all()
manager.view_total()
manager.close()

