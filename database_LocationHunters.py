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

cursor.execute('drop table LocationHunters')
conn.commit()
cursor.execute('''
CREATE TABLE LocationHunters
(
Link nvarchar(4000),
Description nvarchar(4000),
Address nvarchar(4000),
Price int,
Photo TEXT
)
''')
conn.commit()

with open("data_location_hunters1.json", "r") as read_file:
    data1 = json.load(read_file)

for i in data1:
    link = i['link']
    description = i['description']
    photo = i['photo']

    query = "insert into LocationHunters (Link, Description, Photo, Address, Price) values (?, ?, ?, ?, ?)"
    data1 = [(link, description, photo, '', None)]
    cursor.executemany(query, data1)
    conn.commit()

with open("data_location_hunters2.json", "r") as read_file:
    data2 = json.load(read_file)

for i in range(0, len(data2)):
    link = data2[i]['link']
    description = data2[i]['description']
    photo = data2[i]['photo']

    query = "insert into LocationHunters (Link, Description, Photo, Address, Price) values (?, ?, ?, ?, ?)"
    data1 = [(link, description, photo, '', None)]
    cursor.executemany(query, data1)
    conn.commit()

with open("data_location_hunters3.json", "r") as read_file:
    data3 = json.load(read_file)

for i in range(0, len(data3)):
    link = data3[i]['link']
    description = data3[i]['description']
    photo = data3[i]['photo']

    query = "insert into LocationHunters (Link, Description, Photo, Address, Price) values (?, ?, ?, ?, ?)"
    data1 = [(link, description, photo, '', None)]
    cursor.executemany(query, data1)
    conn.commit()

with open("data_location_hunters4.json", "r") as read_file:
    data4 = json.load(read_file)

for i in range(0, len(data4)):
    link = data4[i]['link']
    description = data4[i]['description']
    photo = data4[i]['photo']

    query = "insert into LocationHunters (Link, Description, Photo, Address, Price) values (?, ?, ?, ?, ?)"
    data1 = [(link, description, photo, '', None)]
    cursor.executemany(query, data1)
    conn.commit()