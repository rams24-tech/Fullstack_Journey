from flask import Flask,render_template
import psycopg2

app=Flask(__name__)

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="expense_tracker",
        user="postgres",
        password="Ramadevi@1984"
    )

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/expenses")
def expenses():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses ORDER BY id;")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("expenses.html", expenses=rows)



if __name__ =="__main__":
    app.run(debug=True)