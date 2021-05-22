import pyodbc
import json

def no_space(string):
    new = ''
    for i in string:
        if (i != ' '):
            new += i
    return new


connection_string = "Driver={ODBC Driver 17 for SQL Server};"\
"Server=tcp:84.252.140.138;"\
"Database=Cinema;"\
"uid=ucinema;pwd=P@sswordCinema;"

conn = pyodbc.connect(connection_string)

cursor = conn.cursor()

cursor.execute('drop table TheLocals')
conn.commit()
cursor.execute('''
CREATE TABLE TheLocals
(
Link nvarchar(4000),
Description nvarchar(4000),
Address nvarchar(4000),
Price int,
Photo TEXT
)
''')
conn.commit()

with open("data_thelocals.json", "r") as read_file:
    data = json.load(read_file)

for i in range(len(data)):
    link = data[i]['ссылка']
    description = data[i]['описание']
    price = int(no_space(data[i]['цена аренды в месяц']))
    photo = ''
    for j in range(min(len(data[i]['фото']), 10)):
        photo += data[i]['фото'][j]
        photo += " "
    query = "insert into TheLocals (Link,Description,Price, Photo, Address) values (?, ?, ?, ?, ?)"
    data1 = [(link, description, price, photo, '')]
    cursor.executemany(query, data1)
    conn.commit()


