import pymongo
#open mongodb connection
conn = pymongo.MongoClient('mongodb://localhost:27017')
#print the available mongodb databases
databases = conn.database_names()
for database in databases:
    print(database)

conn.close()
