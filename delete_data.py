import mysql.connector

database = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="Ank123!",
    database="mydatabase"
)

cursorObject = database.cursor()
query = "DELETE FROM student WHERE ROll = 101"
cursorObject.execute(query)
database.commit()
print("Data Deleted Successfully")
database.close()