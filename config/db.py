from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv() 
CONNECTION_STRING = os.environ.get("CONNECTION_STRING")
if not CONNECTION_STRING:
    raise ValueError("No CONNECTION_STRING found in environment variables")

conn = MongoClient(CONNECTION_STRING)
print(CONNECTION_STRING)