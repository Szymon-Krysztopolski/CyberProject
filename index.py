from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Witaj na stronie głównej!'

@app.route('/about')
def about():
    return 'O nas'

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
