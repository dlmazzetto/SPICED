
import random
import time
import logging
from sqlalchemy import create_engine

FRUIT = "apple,banana,orange,pear,melon".split(',')

time.sleep(10)
# hostname : name of the other container!
db = create_engine('postgres://postgres:1234@postgresdb:5432/postgres', echo=True)
#                   DB type    user     psw  host       port dbname

sql = f"CREATE TABLE IF NOT EXISTS fruit ( name VARCHAR(20) );"
db.execute(sql)

while True:
    fruit = random.choice(FRUIT)
    logging.critical(f'here is a fruit: {fruit}')
    sql = f"INSERT INTO fruit VALUES ('{fruit}');"
    db.execute(sql)
    time.sleep(10)
