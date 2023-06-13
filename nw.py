import mysql.connector

# Establishing a connection to the MySQL server
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

# Creating a new database
cursor = connection.cursor()
cursor.execute("CREATE DATABASE deeps")

# Committing the changes and closing the connection
connection.commit()
connection.close()
