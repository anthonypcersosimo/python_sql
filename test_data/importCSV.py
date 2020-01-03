import csv
import ast
import psycopg2
import mysql.connector

f = open('secret.txt', 'r')
if f.mode == 'r':
    secret = f.read()

db_name = 'stocks'

mydb = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',
    db=db_name,
    use_unicode='true',
    username='root',
    passwd=secret
)

if mydb:
    print(f'Connected to SQL Database: {db_name}')

# Create a cursor (an instance) to manipulate your SQL Database
mycursor = mydb.cursor(buffered=True)

# # Create SQL Schema ==========================================
f = open('test_data/sn_buy_rated.csv', 'r')
reader = csv.reader(f)

longest, headers, type_list = [], [], []


def dataType(val, current_type):
    try:
        # Evaluates numbers to an appropriate type, and strings an error
        t = ast.literal_eval(val)
    except ValueError:
        return 'varchar'
    except SyntaxError:
        return 'varchar'
    if type(t) in [int, float]:
        if (type(t) in [int]) and current_type not in ['float', 'varchar']:
           # Use smallest possible int type
            if (-32768 < t < 32767) and current_type not in ['int', 'bigint']:
                return 'smallint'
            elif (-2147483648 < t < 2147483647) and current_type not in ['bigint']:
                return 'int'
            else:
                return 'bigint'

        if type(t) is float and current_type not in ['varchar']:
            return 'decimal'
    else:
        return 'varchar'


for row in reader:
    if len(headers) == 0:
        headers = row
        for col in row:
            longest.append(258)
            type_list.append('')
    else:
        for i in range(len(row)):
            # NA is the csv null value
            if type_list[i] == 'varchar' or row[i] == 'NA':
                pass
            else:
                var_type = dataType(row[i], type_list[i])
                type_list[i] = var_type
        if len(row[i]) > longest[i]:
            longest[i] = len(row[i])
f.close()

statement = 'create table ec_universe ('

for i in range(len(headers)):
    if type_list[i] == 'varchar':
        statement = (
            statement + '\n{} varchar({}),').format(headers[i].lower(), str(longest[i]))
    else:
        statement = (statement + '\n' + '{} {}' +
                     ',').format(headers[i].lower(), type_list[i])

statement = statement[:-1] + ');'

print(statement)
