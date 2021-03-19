from pymongo import MongoClient

#         {"$unwind": "$tags"},
# ...     {"$group": {"_id": "$tags", "count": {"$sum": 1}}},

with MongoClient() as client:
    db = client.library
    pipelines = [
        {"$match": {"status": "PUBLISH"}},
        {"$unwind": "$categories"},
        {"$group": {"_id": "$categories", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
    ]

    books = db.books.aggregate(pipelines)

    print(books)
    for category in db.books.aggregate(pipelines):
        # print(f"{category["id"]} {category["count"]}")
        # print(f'{category['_id']}')
        print(category["_id"], category["count"])
