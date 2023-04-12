
from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient

password = os.environ.get("MONGO_PWD")
connection_string = f"mongodb+srv://kelvynsantos10:{password}@crud.pyl0s0d.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)

dbs = client.list_database_names()
print(dbs)