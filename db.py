import pymongo

connection_string="mongodb://localhost:27017"

client = pymongo.MongoClient(connection_string)

db = client["mydatabase"]

collection = db["mycollection"]

data=[
    {"name":"Sanket",
    "age":21,
    "designation":"Java Programmer"}
]

# collection.insert_many(data)

# print("All records: ")

# cursor= collection.find()

# for document in cursor:
#     print(document)
