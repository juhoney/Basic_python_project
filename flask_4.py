from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

app.secret_key = 'fajdslklksdjklf'

@app.route('/')
def home():
    return "Hello, world"

@app.route('/welcome')
def welcome():
    return render_template(welcome.html)

@app.route('/number', methods=['GET', 'POST'])
def login():
    error = None


    return render_template('number.html', error=error)



@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('welcome'))

if __name__ == '__main__':
    app.run()

