import pymongo
import os
from pymongo import MongoClient
import csv
from datetime import  datetime
client = pymongo.MongoClient("mongodb+srv://m001-student:v0eVQ1r9aRgQf7Px@sandbox-umqdm.mongodb.net/sample_mflix?retryWrites=true&w=majority")
db = client.sample_apitest

users_list = []
for i in range(100):
    val = "users" + str(1) + "logged in"
    users_list.append("users", )


"API token - tujkuupf"

users = db["users"]


print(datetime.now())
print("Connected")
users.insert_many(users_list)

print("Completed")