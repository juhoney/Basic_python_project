from flask.Mul_Table import  Flask

app = Flask(__name__)

@app.route('/honey')
def helloworld():
    return "honeybee"
@app.route('/')
def default_function():
    return "default"

if __name__ == '__main__':
    app.run()