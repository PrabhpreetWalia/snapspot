from flask import render_template, request, redirect, url_for, flash
from __main__ import app
from datetime import datetime

import mysql.connector, json

try:
    con = mysql.connector.connect(host="localhost", user="root", password="toor", database="flask" )
    cur = con.cursor(dictionary = True)
    con.autocommit = True
    print("Database Connected")
except:
    print("Database not connected")


@app.route("/admin", methods = ["GET", "POST"])
def adminPage():
    if request.method == "GET":
        return render_template("admin.html")
    elif request.method == "POST":
        print(request.files['image'])
        if (request.files['image'].filename) == "":
            return render_template("admin.html")
        
        file = request.files["image"]
        file_ext = file.filename.split(".")[1]
        filename = str(datetime.now().timestamp()).replace(".", "") + "."+ str(file_ext)
        file.save(f"static/img/{filename}")
        location = request.form['location']
        cur.execute(f"""INSERT INTO `flask`.`data` (`link`, `location`) VALUES ('../static/img/{filename}', '{location}');""")
        return redirect(url_for("mainPage"))