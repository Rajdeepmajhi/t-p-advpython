import mysql.connector
con = mysql.connector.connect(
    user="root",
    password="Raj@6371",
    host="localhost",
    port=3306,
    database = 'giet'  

)
cur = con.cursor()

#query = "select * from gietudb where address != 'delhi' "
#query = "select * from gietudb where salary BETWEEN 15000 AND 30000"
#query = "select * from gietudb where designation != 'teacher'"
#query = "select * from gietudb where name IN ('aman','naman')"
#query = "select * from gietudb where name LIKE '%a%a%'"
#query = "select * from gietudb where LENGTH(name) = 5"
#query = "select * from gietudb WHERE address LIKE 'r%'"
#query = "select * from gietudb ORDER BY salary DESC LIMIT 3"
#query = "select * from gietudb ORDER BY salary ASC LIMIT 1"
#query = "select SUM(salary) from gietudb WHERE gender='M'"
#query = "select AVG(salary) from gietudb WHERE gender='F'"
#query = "select COUNT(*) from gietudb WHERE salary > 20000"
#query = "select designation, COUNT(*) from gietudb GROUP BY designation"
#query = "select gender, AVG(salary) from gietudb GROUP BY gender"
#query = "select address, SUM(salary) from gietudb GROUP BY address"
#query = "select designation, AVG(salary) from gietudb GROUP BY designation HAVING AVG(salary) > 20000"
query = "select address, COUNT(*) from gietudb GROUP BY address HAVING COUNT(*) > 1"
query = ""
query = ""
query = ""

cur.execute(query)
myresult = cur.fetchall()
for x in myresult:
    print(x)
#cur.close()
con.close()
