from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def myroute():
    return render_template('greet.html')
@app.route('/Contact/')
def contact():
    return render_template('contact.html')
if __name__=='__main__':
    app.run(debug=True)