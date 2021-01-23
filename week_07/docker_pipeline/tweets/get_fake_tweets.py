'''Module generates fake tweets for the Twitter project'''

import time
import logging

# If you wanted to use this line on your local machine you needed to pip install Faker
from faker import Faker
from pymongo import MongoClient

fake = Faker()


# Connection to MongoDB
client = MongoClient(host='mongodb', port=27017)
# host 'mongodb' indicates that we are talking directly to the container mongodb
# of the docker-compose pipeline

# Connecting to the database twitter on mongodb
db = client.twitter # Equivalent to use twitter
# Collection tweets in database twitter
tweets = db.tweets


while True:

    name = fake.name()
    text = fake.text()

    logging.warning('-----INCOMING TWEET!!!!!--------')
    # logging.critical(name)
    # logging.critical(text)
    tweets.insert({'user_name': name, 'text': text})
    logging.critical('SUCCESSFULLY ADDED TO DB!!!!!!')
    logging.warning('--------------------------------')


    time.sleep(3)
    #Make sure you can see this printed in your terminal!
