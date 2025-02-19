import mysql.connector

database = mysql.connector.connect(
    host="HostName",
    user="UserName",
    passwd="Password",
    database="mydatabase"
)

cursorObject = database.cursor()
# limit clause is used to limit the number of rows to be fetched from the table
# query1 fetches the first 3 rows from the table
query1 = "SELECT * FROM student LIMIT 3"
# offset clause is used to skip the number of rows from the table
# query2 fetches the next 3 rows from the table
query2 = "SELECT * FROM student LIMIT 3 OFFSET 3"

cursorObject.execute(query1)
myresult = cursorObject.fetchall()
for x in myresult:
    print(x)

print("\n ________________________ \n")

cursorObject.execute(query2)
result = cursorObject.fetchall()
for y in result:
    print(y)

database.close()
