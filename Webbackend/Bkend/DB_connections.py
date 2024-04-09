import pymongo

url = 'mongodb+srv://fabymtt:fabyecommerce@cluster0.dwb0on0.mongodb.net/'
client = pymongo.MongoClient (url)

db = client['Ecommerce']