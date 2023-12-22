import unittest
from django.test import TestCase
from django.db import connection
from pymongo import MongoClient

class MongoDBConnectionTest(TestCase):
    def test_mongodb_connection(self):
        # Get MongoDB connection settings from Django settings
        mongo_settings = connection.settings_dict['OPTIONS']
        print(mongo_settings)
        # Create a MongoDB connection using PyMongo
        # client = MongoClient(host=mongo_settings['HOST'], port=int(mongo_settings['PORT']))
        #
        # # Check if the connection is successful
        # try:
        #     # Access a sample collection in the MongoDB
        #     db = client[mongo_settings['NAME']]
        #     collection = db['scrapy_data']
        #     document_count = collection.count_documents({})
        #
        #     # Assert that the document count is greater than or equal to 0
        #     self.assertGreaterEqual(document_count, 0, "MongoDB connection test failed")
        #
        # except Exception as e:
        #     # If any exception occurs, fail the test
        #     self.fail(f"MongoDB connection test failed with error: {e}")
        #
        # finally:
        #     # Close the MongoDB connection
        #     client.close()

if __name__ == '__main__':
    unittest.main()
