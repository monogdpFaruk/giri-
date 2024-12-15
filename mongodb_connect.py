from pymongo import MongoClient

class MongoDBConnection:
    def __init__(self,url='mongodb+srv://farookmousa2021:Fbz8d9mEZ6URvFOV@cluster0.lxgcc.mongodb.net/?retryWrites=true&w=majority'):
        self.client = MongoClient(url)

    
    def database_getir(self, db_name):
        return self.client[db_name]