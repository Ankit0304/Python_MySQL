import mysql.connector

database = mysql.connector.connect(
    host="127.0.0.1",
user="root",
passwd="Ank123!",
database="mydatabase"
)

cursorObject = database.cursor()
query = "DROP TABLE IF EXISTS teacher"
cursorObject.execute(query)
database.commit()
print("Table Deleted Successfully")
database.close()