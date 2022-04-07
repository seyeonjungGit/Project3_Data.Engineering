"""

# https://www.elephantsql.com/
# postgres://zadfzycd:BRlAAtNwTbQi3dcIGniQaVg8o0CExXdy@chunee.db.elephantsql.com/zadfzycd
postgres://zadfzycd:BRlAAtNwTbQi3dcIGniQaVg8o0CExXdy@chunee.db.elephantsql.com/zadfzycd
"""

import psycopg2
import csv
# breakpoint()
# DB_FILENAME = 'fitness analysis.csv'
# DB_FILEPATH = os.path.join(os.getcwd(), DB_FILENAME)

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

cur.execute("DROP TABLE IF EXISTS fitness;")
cur.execute("""CREATE TABLE fitness (
                Id  INTEGER NOT NULL PRIMARY KEY,
                Gender VARCHAR(6),
                Age VARCHAR(12),
                Exercise_importance INT,
                Fitness_level VARCHAR(9),
                Regularity VARCHAR(19),
                Do_you VARCHAR(26),
                Time VARCHAR(13),
                Time_spent VARCHAR(23),
                Balanced_diet VARCHAR(10),
                Health_level INT,
                Recommend_fitness VARCHAR(3),
                Equipment VARCHAR(3),
                Barriers VARCHAR(37),
                Exercises VARCHAR(23),
                prevents_balanced VARCHAR(63),
                Motivation VARCHAR(82)              
                )
            """)
import csv
pt = list()
with open('./fitness.csv', encoding='UTF8', newline='') as csvfile:
    reader = csv.reader(csvfile)
    i=0
    for row in reader: 
        li = list(row)
        li.insert(0,i-1)
        tup = tuple(li)
        pt.append(tup)
        i += 1


for user in pt[1:] :
    cur.execute("INSERT INTO fitness (Id, Gender, Age, Exercise_importance, Fitness_level, Regularity, Do_you, Time, Time_spent, Balanced_diet, Health_level, Recommend_fitness, Equipment, Barriers, Exercises,  prevents_balanced,  Motivation ) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);", user)



connection.commit()
connection.close