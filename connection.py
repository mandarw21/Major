from pymongo import MongoClient
class MongoConnection:
    def getConnection():
        try:
            connection = MongoClient("mongodb+srv://admin:root1234@cluster0-3eho0.mongodb.net/test?retryWrites=true")
            print("Connected Successfully")
            db=connection.MajorDatabase
            collection = db.ImageDB
            return collection
        except:   
            print("Could not connect to MongoDB")
