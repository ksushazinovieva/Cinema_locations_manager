import pyodbc
import json

connection_string = "Driver={ODBC Driver 17 for SQL Server};"\
"Server=tcp:84.252.140.138;"\
"Database=Cinema;"\
"uid=ucinema;pwd=P@sswordCinema;"

conn = pyodbc.connect(connection_string)

cursor = conn.cursor()

cursor.execute("select * from TheLocals")
for row in cursor:
    print(row)
conn.commit()