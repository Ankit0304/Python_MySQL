# creating a database in MySQL using Python

import mysql.connector
database = mysql.connector.connect(
    host="HostName",
    user="UserName",
    passwd="Password"
)
# cursor object is used to interact with the database with cursor() method
cursorObject = database.cursor()

# creating a database using the execute() method
cursorObject.execute("CREATE DATABASE mydatabase")