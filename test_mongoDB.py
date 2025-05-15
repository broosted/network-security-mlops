from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()

MONGO_DB_PW = os.getenv("MONGODB_PW")
MONGO_DB_USER = os.getenv("MONGODB_USER")

uri = f"mongodb+srv://{MONGO_DB_USER}:{MONGO_DB_PW}@cluster0.ld7yesa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e) 