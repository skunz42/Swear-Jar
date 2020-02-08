# Sean Kunz
# DB

from pymongo import MongoClient

class DB:
    def __init__(self):
        self.client = MongoClient(port=27017)
        self.db = self.client.HACKBU2020
        self.prog = 0.0
        self.initialize()

    def initialize(self):
        cursor = self.db.progress.find_one({"user": "test"}, {"_id": 0})
        self.prog = float(cursor['amount'])

    def getProgress(self):
        return self.prog

    def setProgress(self):
        self.prog += 0.25

    def writeDB(self):
        self.db.progress.update_one({
            'user': 'test'
        },{
            '$set': {
                'amount': self.prog
            }
        }, upsert=False)
