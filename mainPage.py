from flask import render_template
from __main__ import app
import mysql.connector, json



@app.route("/", methods = ["GET"])
def mainPage():
    try:
        con = mysql.connector.connect(host="localhost", user="root", password="toor", database="flask" )
        cur = con.cursor(dictionary = True)
        print("Database Connected")
    except:
        print("Database not connected")

    cur.execute("SELECT * FROM data")
    result = json.loads(json.dumps(cur.fetchall()))

    return render_template("main.html", data = result)