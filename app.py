from flask import Flask, render_template, jsonify, request
import mysql.connector as database



app = Flask(__name__)

mydb = database.connect(
    host="localhost",
    user="root",
    password="work12GE",
    database="dbuser"
)


@app.route('/hello', methods = ['GET'])
def hello_world():  # put application's code here
    mystatement = mydb.cursor()
    mystatement.execute("SELECT * FROM name;")
    myresult = mystatement.fetchall()
    return jsonify(myresult)


@app.route('/', methods = ['POST', 'GET'])
def hello():
   return render_template("index.html")

@app.route('/clicked', methods = ['POST', 'GET'])
def clicked():
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    cur = mydb.cursor()
    sql = "INSERT INTO name (fname, lname) VALUES (%s, %s)"
    value = (fname, lname)
    cur.execute(sql, value)
    mydb.commit()
    return render_template("clicked.html")




app.run()
