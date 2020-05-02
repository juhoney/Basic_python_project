from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/img', methods=['POST'])
def img_function():
    temp = request.form['img_name']
    return render_template('img_static.html', img=temp)

@app.route('/')
def helloworld():
    return render_template('button_edit.html')

if __name__=="__main__":
    app.run()