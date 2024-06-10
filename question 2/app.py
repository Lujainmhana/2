from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/page1.html')
def page1():
    return render_template('page1.html')

@app.route('/page2.html')
def page2():
    return render_template('page2.html')

@app.route('/page3.html')
def page3():
    return render_template('page3.html')

if __name__ == '__main__':
    app.run(debug=True,port=1234)