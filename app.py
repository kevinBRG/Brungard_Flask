from flask import Flask, render_template, jsonify, request
import mysql.connector as database

app = Flask(__name__)

# provide database access
mydb = database.connect(
    host="85.214.249.86",
    user="user",
    password="R9~J+S$0iJ^f",
    database="dbuser"
)


# reference to login site
@app.route('/', methods=['POST', 'GET'])
def hello():
    return render_template("index.html")


# show all login entrys
@app.route('/hello', methods=['POST', 'GET'])
def hello_world():
    mystatement = mydb.cursor()
    mystatement.execute("SELECT * FROM name;")
    myresult = mystatement.fetchall()
    return jsonify(myresult)


# write login data into database
@app.route('/clicked', methods=['POST', 'GET'])
def clicked():
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    cur = mydb.cursor()
    sql = "INSERT INTO name (fname, lname) VALUES (%s, %s)"
    value = (fname, lname)
    cur.execute(sql, value)
    mydb.commit()
    return render_template("clicked.html")

# app.run()