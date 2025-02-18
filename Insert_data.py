# Inserting a data into the table

import mysql.connector
database = mysql.connector.connect(
    host="HostName",
    user="UserName",
    passwd="Password",
    database="mydatabase"
)

# cursor object created 
cursorObject = database.cursor()

# create a variable to store the SQL query
sql = "INSERT INTO student (NAME, BRANCH, ROLL, SECTION, AGE) VALUES (%s, %s, %s, %s, %s)"
val = ("Ankita", "CSE", 101, "A", 20)

# execute the query
cursorObject.execute(sql, val)
# commit the transaction
database.commit()
# print the number of rows inserted
print(cursorObject.rowcount, "record inserted.")
database.close()