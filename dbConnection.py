from pymongo import MongoClient

class MongoDB:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017') # connect to MongoDB 
        self.db = self.client['sudoku'] # access database

    def get_highscores(self):
        highscores_collection = self.db['highscores']
        # find top 20 scores
        top_20 = highscores_collection.find().sort("score", -1).limit(20) # -1 for descending order
        return top_20
    
    def add_highscore(self, username, score):
        highscores_collection = self.db['highscores']
        highscores_collection.insert_one({"username": username, "score": score})
    
    def find_user(self, username, password):
        users_collection = self.db['users']
        if users_collection.find_one({"name" : username, "password": password}) is not None:
            return True
        else: 
            return False
    
    def add_user(self, username, password):
        # Add a new user
        users_collection = self.db['users']
        users_collection.insert_one({"name": username, "password": password})
    
    def close(self):
        self.client.close()
    