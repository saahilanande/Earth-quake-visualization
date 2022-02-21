import re
from flask import Flask, render_template, request,redirect,url_for
import pyodbc
import json


server = 'tcp:adbsaahilserver.database.windows.net'
database = 'sqldatabase1'
username = 'serveradmin'
password = 'Spa12345'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)


app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def home():
    if request.method == "POST":
            if request.form.get("fbutton"):
                cursor = cnxn.cursor()
                cursor.execute("select (case when mag <= 1 then 'below 1' when mag >= 1 and mag <= 2 then '1 to 2' when mag >= 2 and mag <= 3 then '2 to 3' when mag >= 3 and mag <= 4 then '3 to 4' when mag >= 4 and mag <= 5 then '4 to 5' else 'other' end) as range, count(*) as cnt from all_month group by (case when mag <= 1 then 'below 1' when mag >= 1 and mag <= 2 then '1 to 2' when mag >= 2 and mag <= 3 then '2 to 3' when mag >= 3 and mag <= 4 then '3 to 4' when mag >= 4 and mag <= 5 then '4 to 5' else 'other' end);")
                data = cursor.fetchall()
                y = []
                x = []
                for row in data:
                    y.append(row[1])
                print(y)
                    
                for row in data:
                    x.append(row[0])
                print(x)
                return render_template('home.html',label=x,number=y)

            else:
                
                return render_template('home.html')
    else: 
        return render_template('home.html')

@app.route('/task2', methods=["POST", "GET"])
def task2():
    cursor = cnxn.cursor()
    cursor.execute("select (case when mag <= 1 then 'below 1' when mag >= 1 and mag <= 2 then '1 to 2' when mag >= 2 and mag <= 3 then '2 to 3' when mag >= 3 and mag <= 4 then '3 to 4' when mag >= 4 and mag <= 5 then '4 to 5' else 'other' end) as range, count(*) as cnt from all_month group by (case when mag <= 1 then 'below 1' when mag >= 1 and mag <= 2 then '1 to 2' when mag >= 2 and mag <= 3 then '2 to 3' when mag >= 3 and mag <= 4 then '3 to 4' when mag >= 4 and mag <= 5 then '4 to 5' else 'other' end);")
    data = cursor.fetchall()
    y = []
    x = []
    for row in data:
        y.append(row[1])
        
    for row in data:
        x.append(row[0])

    return render_template('task2.html',label=x,number=y)

@app.route('/task3', methods=["POST", "GET"])
def task3():
    if request.method == "POST":
        if request.form.get("fbutton"):
            cursor = cnxn.cursor()
            cursor.execute("select top 100 mag as x, depth as y from all_month")
            data = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            results = []
            for row in data:
                results.append(dict(zip(columns, row)))
            return render_template('task3.html', scatter=results)
        else:
            return render_template('task3.html')
    else:
        return render_template('task3.html')


if __name__ == '__main__':
    app.run(debug =True)