from pymongo import MongoClient

def get_db(db_name):
  client = MongoClient('mongodb://root:password@mongo:27017')
  return client[db_name]