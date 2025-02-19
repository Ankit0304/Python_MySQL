import mysql.connector

database = mysql.connector.connect(
    host="HostName",
    user="UserName",
    passwd="Password",
    database="mydatabase"
)
# cursor object created
cursorObject = database.cursor()
# query 1 to fetch all the data from the table (It fetch all attributes column from the table)
query1 = "SELECT * FROM student"
# query 2 to fetch only the NAME and BRANCH from the table (It fetch particular attributes column from the table)
query2 = "SELECT NAME, BRANCH FROM student"

# execute the query
cursorObject.execute(query1)
# fetch all the data from the table using variable myresult 
myresult = cursorObject.fetchall()

# print the data
for x in myresult:
    print(x)

print("\n ________________________ \n")
cursorObject.execute(query2)
result = cursorObject.fetchall()
for y in result:
    print(y)

database.close()
