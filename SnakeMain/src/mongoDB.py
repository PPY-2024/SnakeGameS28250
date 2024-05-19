import os
import json

from pymongo import MongoClient
from bson import ObjectId

DB_DIR = os.path.join('../db')
DB_FILE = 'data.json'

client = MongoClient('mongodb://localhost:27017/')
db = client['game_database']
collection = db['game_sessions']


def check_database_existence():
    if os.path.exists(DB_DIR) and os.path.isfile(os.path.join(DB_DIR, DB_FILE)):
        if os.path.getsize(os.path.join(DB_DIR, DB_FILE)) > 0:
            return True
    return False


def read_data_from_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)


def write_data_to_file(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file)


def store_game_result(name, map_size, score):
    collection.insert_one({'name': name, 'map_size': map_size, 'score': score})


def init_database_from_file(filename):
    if check_database_existence():
        data = read_data_from_file(filename)
        if data:
            collection.insert_many(data)


def convert_to_json(documents):
    for doc in documents:
        doc['_id'] = str((doc['_id']))
    return documents


def dump_data_to_file(filename):
    data = list(collection.find())
    data = convert_to_json(data)
    write_data_to_file(filename, data)


def init_database_from_mongo():
    if not check_database_existence():
        if not os.path.exists(DB_DIR):
            os.makedirs(DB_DIR)
        with open(os.path.join(DB_DIR, DB_FILE), 'w') as file:
            json.dump([],file)
    else:
        init_database_from_file(os.path.join(DB_DIR, DB_FILE))