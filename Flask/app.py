from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def Home():
    return render_template('home.html')
@app.route('/intro')
def intro():
    return render_template('intro.html')
@app.route('/upload')
def upload():
    return render_template('upload.html')
@app.route('/home')
def Home1():
    return render_template('home.html')
app.run(debug=True)