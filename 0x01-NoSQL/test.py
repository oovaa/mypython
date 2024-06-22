from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
dbnames = client.list_database_names()
# for dbname in dbnames:
#     print(dbname)

db = client['alx']

print(db.list_collection_names())
