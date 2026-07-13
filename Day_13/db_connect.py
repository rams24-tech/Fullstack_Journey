import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="expense_tracker",
    user="postgres",
    password="Ramadevi@1984"
)

print("Connected to database successfully!")

cursor = connection.cursor()
cursor.execute("DELETE FROM expenses WHERE id = %s;", (6,))
connection.commit()
print("Expense deleted!")


cursor.close()
connection.close()
