import sqlite3
import mysql.connector
print('connected!')

f=open("secret.txt","r")
if f.mode == "r":
    secret = f.read() 

mydb = mysql.connector.connect(
    user='root',
    password=secret,
    host='127.0.0.1',
    database='python'
)
print(mydb)
table_name = 'russell3000'

# Create a cursor (an instance) to manipulate your SQL Database
mycursor = mydb.cursor(buffered=True)
