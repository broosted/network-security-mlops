import os
import sys
import json

from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient

load_dotenv()

MONGO_DB_PW = os.getenv("MONGODB_PW")
MONGO_DB_USER = os.getenv("MONGODB_USER")

uri = f"mongodb+srv://{MONGO_DB_USER}:{MONGO_DB_PW}@cluster0.ld7yesa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)

import certifi

ca = certifi.where()

import pandas as pd
import numpy as np
import pymongo

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


class NetworkDataExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def csv_to_json_convertor(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = json.loads(data.T.to_json()).values()
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def insert_data_to_mongo_db(self, records, database, collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records
            self.mongo_client = MongoClient(uri)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            logging.info(f"Data inserted successfully in {self.database} database and {self.collection} collection {len(self.records)} records")
            return "Data inserted successfully"
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        


if __name__ == "__main__":
    network_data_extract = NetworkDataExtract()
    data_file_path = "Network_data/phishingData.csv"
    database = "mongodb_ns"
    collection = "Network_data"
    records = network_data_extract.csv_to_json_convertor(data_file_path)
    network_data_extract.insert_data_to_mongo_db(records, database, collection)
    print("Data inserted successfully")