from pymongo import MongoClient

def get_connection():
    """

    :rtype: object
    """
    return MongoClient()
