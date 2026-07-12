import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="expense_tracker",
    user="postgres",
    password="Ramadevi@1984"
)

print("Connected to database successfully!")

cursor = connection.cursor()
cursor.execute("SELECT * FROM expenses;")
rows = cursor.fetchall()

for row in rows:
    print(f"ID: {row[0]} | {row[1]} | ${row[2]} | {row[3]}")


cursor.close()
connection.close()
