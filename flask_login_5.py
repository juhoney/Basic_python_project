"""
로그인 하는 코드
"""

from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

app.secret_key = 'fajdslklksdjklf'

@app.route('/')
def home():
    return "Hello, world"

n = ['gram', 'login']
m = ['gram', 'login']
flag = 0

def check_test(n, m, flag):
    for i in range(len(n)):
        if request.form['username'] == n[i] and request.form['password'] == m[i]:
            flag = 1
            break
    if flag == 1:
        return True
    else:
        return False

@app.route('/welcome')
def welcome():
    return render_template(welcome.html)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if not session.get('logged_in'):
        if request.method == 'POST':
            if check_test(n, m, flag):
                session['logged_in'] = True
                return redirect(url_for('home'))
            else:
                error = 'Invealid credentials Please try again'
        return render_template('mode.html', error=error)
    else:
        return redirect(url_for('home'))


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('welcome'))

if __name__ == '__main__':
    app.run()

