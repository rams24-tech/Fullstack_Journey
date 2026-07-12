import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="expense_tracker",
    user="postgres",
    password="Ramadevi@1984"
)

print("Connected to database successfully!")

cursor = connection.cursor()
cursor.execute("INSERT INTO expenses (description, amount) VALUES (%s, %s);", ("Dinner", 15.00))
connection.commit()
print("Expense inserted!")

cursor.close()
connection.close()
