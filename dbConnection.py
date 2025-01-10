from pymongo import MongoClient
import bcrypt

class MongoDB:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017') # connect to MongoDB 
        self.db = self.client['sudoku'] # access database

    def get_highscores(self):
        highscores_collection = self.db['highscores']
        # find top 20 scores
        top_20 = highscores_collection.find().sort("score", -1).limit(20) # -1 for descending order
        return list(top_20)
    
    def add_highscore(self, username, score):
        highscores_collection = self.db['highscores']
        highscores_collection.insert_one({"username": username, "score": score})
    
    def find_user(self, username, password):
        users_collection = self.db['users']
        user = users_collection.find_one({"name": username})
        if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
            return True
        else: 
            return False
    
    def add_user(self, username, password):
        users_collection = self.db['users']
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        users_collection.insert_one({"name": username, "password": hashed_password})
    
    def close(self):
        self.client.close()
    