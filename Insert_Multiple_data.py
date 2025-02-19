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
# multiple data to be inserted
val = [
    ("Ankit", "CSIT", 103, "A", 20),
    ("Rahul", "CSIT", 104, "B", 21),
    ("Priya", "CSIT", 105, "A", 22),
    ("Rohan", "CSIT", 106, "B", 23),
    ("Rajeev", "CSIT", 107, "A", 24)
]
# to execute the many data query we use executemany() method
cursorObject.executemany(sql, val)
# commit the transaction
database.commit()
# print the number of rows inserted
print(cursorObject.rowcount, "record inserted.")
# close the connection
database.close()