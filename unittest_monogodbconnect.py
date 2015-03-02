#Installation Instructions

#Windows:
#https://pypi.python.org/packages/2.7/p/pymongo/pymongo-2.8.win-amd64-py2.7.exe#md5=a2300efcc821260e7e739a0cbdea624b

#Linux:
#pip install pymongo

#Install Docs: 
#http://api.mongodb.org/python/current/installation.html

from pymongo import MongoClient

mongo_username = ''
mongo_password = ''
mongo_ip = ''
mongo_port = ''

mongo_uri = 'mongodb://' + mongo_username + ':' + mongo_password + '@' + mongo_ip + ':' + mongo_port
print mongo_uri

mongo_db = ''
mongo_collection = ''

#clientrt = MongoClient('mongodb://root:OqkVBsTKj6TK@54.149.225.22:27017')
clientrt = MongoClient(mongo_uri)
db = clientrt[mongo_db]
collection = db[mongo_collection]
print collection.find_one()
