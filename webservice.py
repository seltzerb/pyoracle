#!/usr/bin/env python
from flask import Flask
import cx_Oracle

app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
    con = cx_Oracle.connect('python/python@172.24.50.231/demodb')
    cur = con.cursor()
    content = """
<link rel=stylesheet type=text/css href="http://127.0.0.1:5000/static/style.css">
<p>Connected to Oracle {0}</p>
<p>Retrieving 20 Records...</p>
<table><tr><th>FirstName</th><th>LastName</th><th>Email</th></tr>
    """.format(con.version)
    cur.execute('SELECT CUST_FIRST_NAME, CUST_LAST_NAME, CUST_EMAIL from oe.customers where ROWNUM < 21 order by CUST_LAST_NAME')
    for result in cur:
        content = content + '<tr><td>' + result[0] + '</td><td>' + result[1] + '</td><td>' + result[2] + '</td></tr>'
    content = content + '</table><p>'+ str(cur.rowcount) + ' rows returned</p>'
    return content

if __name__ == '__main__':
    app.run(host='0.0.0.0')
