import mysql.connector
database = mysql.connector.connect(
     host="HostName",
    user="UserName",
    passwd="Password",
    database="mydatabase"
)
# cursor object is used to interact with the database with cursor() method
cursorObject = database.cursor()

# creating a table
studentRecord = """CREATE TABLE student(
                NAME  VARCHAR(20) NOT NULL,
                BRANCH VARCHAR(50),
                ROLL INT NOT NULL,
                SECTION VARCHAR(5),
                AGE INT
                )"""

# creating a table using the execute() method
cursorObject.execute(studentRecord)
print("Table created successfully")
# disconnecting from the server
database.close()


