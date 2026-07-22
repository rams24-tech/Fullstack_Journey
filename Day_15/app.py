from flask import Flask,render_template,request,redirect,url_for
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
    cursor.execute("SELECT SUM(amount) FROM expenses;")
    total = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return render_template("expenses.html", expenses=rows, total=total)

@app.route("/add", methods=["GET", "POST"])
def add_expense():
    if request.method == "POST":
        description = request.form["description"]
        amount = request.form["amount"]
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO expenses (description, amount) VALUES (%s, %s);", (description, amount))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for("expenses"))
    return render_template("add.html")


if __name__ =="__main__":
    app.run(debug=True)