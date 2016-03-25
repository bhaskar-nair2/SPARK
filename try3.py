import pyodbc as base

config={"user":"root","password":"","host":"127.0.0.1","database":"devloping_spark"}

con=base.connect("DRIVER={SQL Server};SERVER=MySQLServer1;DATABASE=devloping_spark;UID=bhaskar;PWD=")
cur=con.cursor()

cursor.execute("select * from waste")

rows=cursor.fetchone()
print row[1]
 
##CREATE SERVER MySQLServer1
##FOREIGN DATA WRAPPER mysql
##OPTIONS (USER 'bhaskar', HOST '192.168.10.10', DATABASE 'devloping_spark');
