import pymongo

client =pymongo.MongoClient('mongodb://localhost:27017/')



dblist = client.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")
