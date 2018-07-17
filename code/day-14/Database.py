import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  )

print(mydb.user)