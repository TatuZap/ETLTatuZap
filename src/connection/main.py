import pymongo
from pymongo import MongoClient

def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "mongodb+srv://tatuzap:joaovitor@cluster0.dw7svve.mongodb.net/?retryWrites=true&w=majority"
                     
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['tatuzap']
  
# This is added so that many files can reuse the function get_database()
#if name == "main":   
  
   # Get the database
dbname = get_database()

collection_turmas = dbname["turmas"]

item_details = collection_turmas.find()
for item in item_details:
   # This does not give a very readable output
   print(item)