from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
# login -> join -> login -> welcome (연예인 닮을꼴 나오기)

conn = sqlite3.connect('database.db')
print("Opened database successfully")
conn.execute("CREATE TABLE IF NOT EXISTS shopping (item TEXT,num TEXT, price TEXT)")
print("Table created successfully")
conn.close()

app = Flask(__name__)

# session 을 설정 안하면 에러가 난다.
app.secret_key = b'1234abc'

con = sqlite3.connect("join_info.db")
cur = con.cursor()

# SQL 쿼리 실행
# CREATE TABLE 테이블명(변수명 변수 자료형, )
try:
    cur.execute("CREATE TABLE namgil(ID  text PRIMARY KEY , PW text, MONEY text)")
    con.commit()
# Connection 닫기
    con.close()
except:
    print("already db")
temp_id = None
@app.route('/', methods=['GET', 'POST'])
def login():
    global temp_id
    error = None
    if not session.get('logged_in'):
        if request.method == 'POST':

            con = sqlite3.connect("join_info.db")
            cur = con.cursor()

            login_id = request.form.get('id', "not data")
            login_pwd = request.form.get('pwd', "not data")

            if login_id == "not data":
                return render_template('login.html')

            # make execute
            print("login_id", login_id)
            test = "SELECT * FROM namgil where ID =(?)"
            cur.execute(test, [login_id])
            rows = cur.fetchall()
            con.commit()
            con.close()

            try:
                if rows[0][1] == login_pwd:
                    print("Sucees Login")
                    session['logged_in'] = True
                    temp_id = login_id
                    return redirect(url_for('addrec'))
            except:
                print("Fail Login")
                return render_template('login.html')
    else:
        return redirect(url_for('addrec'))

    return render_template('login.html', error=error)

@app.route("/sing_up", methods=['POST'])
def sing_up():
    if request.method == 'POST':
        # Compare with
        con = sqlite3.connect("join_info.db")
        cur = con.cursor()

        want_id = request.form.get('want_id', "not data")
        want_pwd = request.form.get('want_pwd', "not data")

        if want_id == "not data":
            return render_template('join.html')
        # make execute
        try:
            execute = "INSERT INTO namgil(ID, PW, MONEY)VALUES(?,?,?)"
            cur.execute(execute, (want_id, want_pwd, 10000))
            print("Success Join")
            con.commit()
            con.close()
            return redirect(url_for('login'))
        except:
            print("Fail Join")
            return render_template('join.html')

@app.route('/welcome')
def welcome():
    return "welcome"

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('welcome'))

@app.route('/shopping', methods=['POST'])
def shopping():
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from shopping")
    rows = cur.fetchall()
    print("DB:")
    print(rows)
    return render_template('sh_list.html', rows = rows)

@app.route('/addrec', methods = ['POST', 'GET'])
def addrec():
    msg = ""
    if request.method == 'POST':
        print("hi post")
        try:
            item = request.form['item']
            num = request.form['num']
            price = request.form['price']

            with sqlite3.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO shopping (item, num, price) VALUES (?, ? ,?)", (item, num, price))
                con.commit()
                msg = "Recod successfully added"
                print("msg", msg)
                return render_template("shopping_add_result.html", message=msg)
        except:
            con.rollback()
            msg = "Error in insert operation"
            print("msg", msg)

            return  render_template("shopping_add_result.html", message=msg)
    else:
        msg = ""
        print("msg", msg)

        return render_template("shopping_add_result.html", message=msg)

@app.route('/pay', methods=['POST'])
def pay():
    global temp_id
    print("temp_id", temp_id)

    con = sqlite3.connect("join_info.db")
    cur = con.cursor()

    test = "SELECT * FROM namgil where ID =(?)"
    cur.execute(test, [temp_id])
    rows = cur.fetchall()
    con.commit()
    con.close()
    print("rows", rows)

    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from shopping")
    rows = cur.fetchall()
    #                cur.execute("INSERT INTO shopping (item, num, price) VALUES (?, ? ,?)", (item, num, price))

    for row in rows:
        print("row item ", row['item'])
        print('row num', row['num'])
        print('row price', row['price'])
    #if rows[0][2] >

if __name__ == '__main__':
    app.run()