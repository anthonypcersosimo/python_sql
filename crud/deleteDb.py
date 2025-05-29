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

# Print a list of all avail databases for given PORT and HOST above
mycursor.execute('SHOW DATABASES')
for x in mycursor:
    print(x)

# DELETE DATA FROM DATABASE ===========================
# Delete data from a table where (params)
# record_to_delete = 'AA'
# query = f'DELETE FROM {table_name} WHERE Ticker = "{record_to_delete}"'

# mycursor.execute(query)

mydb.commit()

print(f'{mycursor.rowcount} records deleted!')