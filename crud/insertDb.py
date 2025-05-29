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
# mycursor.execute('SHOW DATABASES')
# for x in mycursor:
#     print(x)

# Creating a table in the database
# mycursor.execute('DROP TABLE russell3000')
mycursor.execute(
    'CREATE TABLE russell3000 (Ticker VARCHAR(255), Company_Name VARCHAR(255), Price INT, Sector VARCHAR(255), EC_Unique INT PRIMARY KEY)')


# # STORE NEW INFO IN DATABASE ==========================
# Commit data one-time to memory to pass into database
tick = 'UGI'
companyName = 'UGI Resources Inc.'
px = 12
sector = 'Gas'
unique = 1

# Commit multiple rows of data to memory to pass into database
multiple_records = [
    ('SDRL', 'Seadrill Inc.', 229, 'Technology', 2),
    ('AA', 'Alcoa Corp.', 935, 'Gas', 3),
    ('INO', 'Inovio Pharmaceuticals', 22, 'Pharmaceuticals', 4),
    ('AXP', 'American Express Inc.', 49, 'Banks', 5),
    ('VZ', 'Verizon Comm Inc.', 13, 'Communications', 6),
    ('SPWH', 'Sportsmans Wearhouse Inc.', 51, 'Retail', 7),
    ('BA', 'Boeing Co.', 223, 'Industrials', 8),
    ('JPM', 'JPMorgan Chase Inc.', 204, 'Banks', 9),
    ('GS', 'Goldman Sachs Inc.', 347, 'Banks', 10),
    ('RTN', 'Raytheon Corp.', 219, 'Industrials', 11),
    ('EAGL', 'American Eagle Co.', 21, 'Retail', 12),
    ('ODST', 'Offshore Drilling Corp.', 18, 'Gas', 13),
    ('AAPL', 'Apple Inc.', 836, 'Technology', 14),
    ('TEL', 'TelComm Inc.', 7, 'Communications', 15),
    ('T', 'AT&T Inc.', 16, 'Communications', 16)
]

# Store query and data as variables
store_query = 'INSERT INTO russell3000(Ticker, Company_Name, Price, Sector, EC_Unique) VALUES (%s, %s, %s, %s, %s)'
single_record = (tick, companyName, px, sector, unique)

# Pass variables neatly into database
# Single Row
mycursor.execute(store_query, single_record)
# Multiple Rows
mycursor.executemany(store_query, multiple_records)

# mydb.commit() is required to make the changes, otherwise no changes are made to the table.
mydb.commit()

# Print!
print(mycursor.rowcount + 1, 'records inserted!')
print('==================')

