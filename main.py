from flask import Flask,session,redirect,render_template,request,flash
import mysql.connector
app=Flask(__name__)
config = {
  'user': '89Md18ICYd',
  'password': 'dhFpEPgWd1',
  'host': 'remotemysql.com',
  'database': '89Md18ICYd'
}
app.secret_key = 'many random bytes'
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        session['username']=request.form['username']
        session['passw']=request.form['passw']
        print(session['username'])
        mydb=mysql.connector.connect(**config)
        mycursor=mydb.cursor()
        mycursor.execute("""SELECT * FROM test WHERE username LIKE '{}' AND passw LIKE '{}'""".format(session['username'],session['passw']))
        val=mycursor.fetchall()
        mycursor.close()
        mydb.close()
        if(len(val)!=0):
            msg=session['username']
            return render_template('dashboard.html',msg=msg)
        else:
            return redirect('/login')
    return render_template('login.html')
@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        msg=session['username']
        return render_template('dashboard.html',msg=msg)
    else:
        msg1='pls login'
        #flash("pls login")
        return render_template('index.html',msg1=msg1)
        #return redirect('/')
    return render_template('dashboard.html')
@app.route('/logout')
def logout():
    session.pop('username', None)
    msg='logged out'
    return render_template('index.html',msg=msg)
if __name__=='__main__':
    app.run(host='192.168.0.101')
        
