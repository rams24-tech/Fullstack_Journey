import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="expense_tracker",
    user="postgres",
    password="Ramadevi@1984"
)

print("Connected to database successfully!")

cursor = connection.cursor()
cursor.execute("UPDATE expenses SET amount = %s WHERE id = %s;", (6.00, 5))
connection.commit()
print("Expense updated!")

cursor.close()
connection.close()
