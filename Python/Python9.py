import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="datagrokr@123",
  database="db"
)

print(mydb)

mycursor = mydb.cursor()

def getdata():
  mycursor.execute("SELECT * FROM ACTOR")
  for x in mycursor:
          yield x

for i in getdata():
  print(i)