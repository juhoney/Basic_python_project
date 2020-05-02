from flask import Flask, render_template

app = Flask(__name__)
temp_list = []
for a in range(1,10):
    for i in range(1,10):
        temp_list.append("{} x {} = {}".format(a, i, a*i))

@app.route('/')
def default_function():
    return render_template('for_loop.html', len=len(temp_list),
                           temp_list=temp_list)

if __name__=='__main__':
    app.run()
