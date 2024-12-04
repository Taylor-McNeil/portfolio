from pymongo import MongoClient
from dotenv import load_dotenv
import os

#load environment varibales from .env
load_dotenv()

#MongoDB connection
MONGO_URI = os.getenv("MONGO_URI")
if not MONGO_URI:
    raise ValueError("MONGO_URI environment variable not set.")

client = MongoClient(MONGO_URI)
db_books = client["Clearwater_Library"] # The database name
books_collection = db_books["Books"] # The collection name
counters = db_books["Counters"]