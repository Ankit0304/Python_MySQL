import mysql.connector

database = mysql.connector.connect(
    host="HostName",
    user="UserName",
    passwd="Password",
    database="mydatabase"
)
# cursor object created
cursorObject = database.cursor()
# query to fetch the data from the table where BRANCH is 'CS
query = "SELECT * FROM student WHERE BRANCH = 'CSIT'"
# execute the query
cursorObject.execute(query)
# fetch all the data from the table using variable myresult
myresult = cursorObject.fetchall()
# print the data
for x in myresult:
    print(x)

database.close()