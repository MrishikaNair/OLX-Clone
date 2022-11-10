from crypt import methods
from unittest import result
from flask import Flask, flash, request, render_template, redirect, url_for, session
# import mysql.connector

# olx_db=mysql.connector.connect(
#     host="localhost", user="root:"
# )

app = Flask(__name__)

@app.route('/')
def entry_point():
    return render_template('login.html')


@app.route('/form_login', methods=['POST'])
def login():
    username=request.form['username']
    pwd=request.form['password']

    print(username, pwd)

    # cur=mysql.connection.cursor()
    # result=cur.execute("SELECT*FROM users where username=%s and password = %s", (username, pwd))
    result = True
    if result:
            return render_template('sell_buy.html') 
    else:
        return render_template('login.html', info="Invalid Username/Password")
    

@app.route('/sellorbuy', methods=['POST','GET'])
def sellbuy():
    option = request.form['sellbuy']
    if str(option) is '1':
        return render_template('home.html')
    else:
        return render_template('buy1.html')

@app.route('/home', methods=['POST', 'GET']) 
def home():
    return render_template('home.html')

@app.route('/sell1', methods=['POST', 'GET']) 
def sell1():
    return render_template('Sell1.html')

@app.route('/sell2', methods=['POST', 'GET'])
def sell2():
    option = request.form['sellcat']
    return render_template('sell2.html')
    

@app.route('/buy1', methods=['POST', 'GET']) 
def buy1():
    return render_template('buy1.html')

@app.route('/offer', methods=['POST', 'GET']) 
def offer():
    return render_template('offer.html')

@app.route('/post', methods=['POST', 'GET']) 
def post():
    return render_template('post.html')

@app.route('/setting', methods=['POST', 'GET']) 
def setting():
    #username=request.form['name']
    #pwd=request.form['password']
    #n_pwd=request.form['n_password']

    #print(username, pwd)
    
    # cur=mysql.connection.cursor()
    # result=cur.execute("SELECT*FROM users where username=%s and password = %s", (username, pwd))
    result = False
    if result is True:
            return render_template('change.html') 
    else:
        return render_template('Setting.html', info="Invalid Username/Password")



if __name__ == '__main__':
    app.run(debug=True)

