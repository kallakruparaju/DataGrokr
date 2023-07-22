import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="datagrokr@1234",
  database="sakila"
)

print(mydb)

mycursor = mydb.cursor()

def getdata():
  mycursor.execute("SELECT * FROM ACTOR")
  #myresult = mycursor.fetchall()
  for x in mycursor:
          yield x

for i in getdata():
  print(i)