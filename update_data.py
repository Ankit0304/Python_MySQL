import mysql.connector

database = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="Ank123!",
    database="mydatabase"
)

cursorObject = database.cursor()
query = "UPDATE student SET BRANCH = 'CSIT' WHERE BRANCH = 'CSE'"
cursorObject.execute(query)
database.commit()

database.close()