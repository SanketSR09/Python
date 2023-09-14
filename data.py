import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017")

db=client["mydatabase"]
collection=db["mycollection"]

data={
    "name":"Sanket", "age":21, "designation":"Developer",
    "name":"Sankita","age":22, "designation":"Banker"
}

# collection.insert_many(data)

result=collection.find()
for i in result:
    print(i)