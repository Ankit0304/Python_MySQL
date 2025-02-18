# we connecting MySQL using connect() method from mysql.connector module.
# importing the mysql.connector module.
import mysql.connector
# connect to the database
database = mysql.connector.connect(
    host="HostName",
    user="UserName",
    passwd="Password"
)

print(database)
# close the connection
database.close()