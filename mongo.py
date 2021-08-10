import os
import pymongo
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDB"
COLLECTION = "celebrities"


# Connect to database
def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could no connect do MongoDBV: %s") % e


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]


# * INSERT
"""
new_doc = {"first": "douglas", "last": "adams", "dob": "11/03/1952", "hair_color": "gray", "occupation": "writer", "nationallity": "british"}

coll.insert(new_doc)
"""


# * INSERT MORE
"""
new_docs = [{
    "first": "terry",
    "last": "pratchett",
    "dob": "28/04/1948",
    "gender": "m",
    "hair_color": "not much",
    "occupation": "writer",
    "nationallity": "british"
}, {
    "first": "geogre",
    "last": "rr martin",
    "dob": "20/09/1948",
    "gender": "m",
    "hair_color": "white",
    "occupation": "writer",
    "nationallity": "american"
}]

coll.insert_many(new_docs)
"""


# * Find specific data
"""
documents = coll.find({"first": "douglas"})
"""


# * FIND ALL
"""
documents = coll.find()
"""


# * DELETE DATA
"""
coll.remove({"first": "douglas"})
"""


# * UPDATE DATA
"""
coll.update_one({"nationallity": "american"}, {"$set": {"hair_color": "maroon"}})
"""


# * UPDATE MANY
coll.update_many({"nationallity": "american"}, {"$set": {"hair_color": "maroon"}})


documents = coll.find({"nationallity": "american"})

for doc in documents:
    print(doc)