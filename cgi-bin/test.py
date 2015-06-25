import sqlite3,string,cgi,random

connector= sqlite3.connect("test.db")
cursor=connector.cursor()
cursor.execute("create table if not exists People(name text,tel text)")

form =cgi.FieldStorage()
if "name" in form :
  cursor.execute("insert into Pelple values(?,?)",(form["name"].value,form["tel"].value))
print "Content-Type: text/html/n",
print "<html><body>",
cursor.execute("select * from People")
results= cursor.fetchall()
for row in results:
    print (row[0],row[1],"<br>")
print('<form method="post" action="test.py">')
print('<p>name:<input type ="text" name="name">')
print('  tel :<input type ="text" name="tel"></p>')
print('<input type ="submit" value="add" name="button">')
print ('</form>')
print ('</body></html>')


cursor.close();
connector.commit();
connector.close();