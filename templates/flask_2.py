from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def helloworld():
    return render_template('intro_2.html')

@app.route('/namgil', methods=['POST'])
def cal():
    temp = request.form['hello']
    if temp == "hello":
        return "bye"
    else:
        return "nice to meet you"
if __name__ == '__main__':
    app.run()