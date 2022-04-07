import psycopg2
import csv
# breakpoint()

host = 'chunee.db.elephantsql.com'
user = 'zadfzycd'
password = 'BRlAAtNwTbQi3dcIGniQaVg8o0CExXdy'
database = 'zadfzycd'

connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=database
)
# breakpoint()
cur = connection.cursor()

sql = "COPY (SELECT * FROM fitness) TO STDOUT WITH CSV DELIMITER ',' HEADER"
with open("./fitness_export.csv", "w", encoding='UTF8') as file:
    cur.copy_expert(sql, file)

# https://stackoverflow.com/questions/49610908/exporting-a-postgresql-query-to-a-csv-file-using-python
# https://brownbears.tistory.com/136

connection.commit()
connection.close


#https://www.postgresqltutorial.com/export-postgresql-table-to-csv-file/