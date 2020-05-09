import sqlite3
from flask import Flask
from flask import render_template, request

# conn = sqlite3.connect('database.db')
# print('Opened database successfully')
# conn.execute('CREATE TABLE IF NOT EXISTS shopping (item TEXT , num TEXT, price TEXT)')
# print("Table created successfully")
# conn.close()

app = Flask(__name__)

@app.route('/')
def hi():
    return "hello"
a = ['gram']
b = ['gram']


@app.route('/login')
def login():
    if a == 'gram':
        "username login successfully"
    elif b == 'gram':
        "login"
@app.route('/shopping')
def temp_shopping():
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur = cur.execute("select * from shopping")
    rows = cur.fetchall()
    print("rows", rows)
    return render_template('sh_list.html', rows=rows)

@app.route('/database_add', methods = ['POST', 'GET'])
def database_add():
    msg = ""
    if request.method == 'POST':
        try:
            item = request.form['item']
            num = request.form['num']
            price = request.form['price']
            with sqlite3.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO shopping (item, num, price) VALUES (?, ?, ?)", (item, num, price))
                con.commit()
                msg = "Recod successfully added"
                con.close()
        except:
            con.rollback()
            msg = "Error in insert operation"
        finally:
            return render_template("sh_list.html", message=msg)

if __name__== '__main__':
    app.run()