import sqlite3

conn=sqlite3.connect('test1.db')

c=conn.cursor()

q='''SELECT * FROM mytable'''
c.execute(q)

from contextlib import closing
with closing(conn.cursor()) as c:
    q='''SELECT * FROM  mytable'''
    c.execute(q)

with closing(conn.cursor()) as c:
    q='''SELECT * FROM  mytable'''
    c.execute(q)
    result=c.fetchall()

for item in result:
    print(str(item[0]),"|",item[1])

with closing(conn.cursor()) as c:
    q='''SELECT * FROM mytable WHERE id=1'''
    c.execute(q)
    result=c.fetchone()
print(result)

#How to run a query with a parameter

with closing(conn.cursor()) as c:
    q='''SELECT * FROM mytable WHERE id=?'''
    c.execute(q,(2,))
    result=c.fetchall()

for item in result:
    print(str(item[0]),"|",item[1])

#Execute an INSERT statement and search the new record

id=6
name="mike"

with closing(conn.cursor()) as c:
    q='''INSERT INTO mytable (id,name) VALUES (?,?)'''
    c.execute(q,(id,name))
    conn.commit()

with closing(conn.cursor()) as c:
    q='''SELECT * FROM mytable WHERE id=?'''
    c.execute(q,(6,))
    result=c.fetchall()

for item in result:
    print(str(item[0]),"|",item[1])

# Execute an UPDATE statement and display all records.
id=6
name="prince"
with closing(conn.cursor()) as c:
    q='''UPDATE mytable 
    SET name=?
    WHERE id=?
    '''
    c.execute(q,(id,name))
    conn.commit()

with closing(conn.cursor()) as c:
    q='''SELECT * FROM mytable'''
    c.execute(q,(6,))
    result=c.fetchall()

for item in result:
    print(str(item[0]),"|",item[1])

# DELETE the record id=6 and display all records.
id=6

with closing(conn.cursor()) as c:
    q='''DELETE FROM mytable WHERE id=?'''
    c.execute(q,(id,))
    conn.commit()

with closing(conn.cursor()) as c:
    q='''SELECT * FROM mytable WHERE id=?'''
    c.execute(q,(6,))
    result=c.fetchall()

for item in result:
    print(str(item[0]),"|",item[1])