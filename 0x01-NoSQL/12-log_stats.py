from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client.logs
colec = db.nginx

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

logs = colec.count_documents({})

m_data = {m: colec.count_documents({'method': m}) for m in methods}

special = colec.count_documents({'method': 'GET', 'path': '/status'})

print(logs, 'logs')


print('Methods:')

for m, c in m_data.items():
    print(f'\tmethod {m}: {c}')
print(special, 'status check')
