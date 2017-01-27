#!/usr/bin/env python
import cx_Oracle
con = cx_Oracle.connect('python/python@172.24.50.231/demodb')
print con.version
cur = con.cursor()
#cur.execute('SELECT owner, table_name FROM dba_tables')
cur.execute('SELECT CUST_FIRST_NAME, CUST_LAST_NAME, CUST_EMAIL from oe.customers where ROWNUM < 51 order by CUST_LAST_NAME')

for result in cur:
    print result
print cur.rowcount
cur.close()
con.close()
