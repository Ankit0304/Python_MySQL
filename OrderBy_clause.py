import mysql.connector

database = mysql.connector.connect(
    host="HostName",
    user="UserName",
    passwd="Password",
    database="mydatabase"
)

cursorObject = database.cursor()
# query to fetch the data from the table in descending order
query = "SELECT * FROM student ORDER BY NAME DESC"

cursorObject.execute(query)

myresult = cursorObject.fetchall()
for x in myresult:
    print(x)
    
database.close()