def insert_school(mongo_collection, **kwargs):
    return mongo_collection.insert_one(kwargs)
