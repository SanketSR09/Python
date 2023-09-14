import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017")

db=client["SSR"]

collection=db["family"]

data=[{
    "name":"Sanket","age":21,"relation":"me"},
    {"name":"Sankita","age":22,"relation":"sister"},
    {"name":"Kavita","age":47,"relation":"mother"},
    {"name":"Sanjay","age":51,"relation":"father"
}]

# collection.insert_many(data)

# result=collection.find()
# for i in result:
#     print(i)

# query={"age":{"$gt":50}}
# result= collection.find(query)

# for i in result :
#     print(i)

# query={"age":51}
# collection.delete_one(query)

query={"name":"Sanjay"}
new_data={"$set":{"age":50}}

collection.update_one(query,new_data)