from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/<int:num>')
def helloworld(num=None):
    return render_template('intro_3.html',num=num)

@app.route('/cal', methods=['POST'])
def namgil():
    temp = request.form['hello']
    if request.method == 'POST':
        return redirect(url_for('helloworld', num=temp))

if __name__ == '__main__':
    app.run()

#함수 하나 만들기