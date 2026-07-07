from __future__ import annotations

import random
from typing import List, Dict, Any

from pymongo import MongoClient
from pymongo.errors import PyMongoError

MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "shop"
COLLECTION_NAME = "products"
CATEGORIES = ["Electronics", "Books", "Clothes"]


def generate_products() -> List[Dict[str, Any]]:
    products: List[Dict[str, Any]] = []
    for i in range(1, 51):
        quantity = random.randint(0, 100)
        product = {
            "name": f"Product {i}",
            "category": random.choice(CATEGORIES),
            "price": random.randint(50, 3000),
            "quantity": quantity,
            "available": quantity > 0,
        }
        products.append(product)
    return products


def main() -> None:
    try:
        client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        client.admin.command("ping")
    except PyMongoError as exc:
        print(f"Unable to connect to MongoDB at {MONGO_URI}: {exc}")
        print("Start MongoDB locally and run the script again.")
        return

    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]

    collection.delete_many({})
    products = generate_products()
    collection.insert_many(products)

    print("All products:")
    for product in collection.find({}, {"_id": 0}):
        print(product)

    print("\nAvailable products:")
    for product in collection.find({"available": True}, {"_id": 0}):
        print(product)

    print("\nProducts with price greater than 1000:")
    for product in collection.find({"price": {"$gt": 1000}}, {"_id": 0}):
        print(product)

    print("\nCount by category:")
    counts = list(collection.aggregate([
        {"$group": {"_id": "$category", "count": {"$sum": 1}}},
        {"$sort": {"_id": 1}},
    ]))
    for item in counts:
        print(f"{item['_id']}: {item['count']}")

    collection.update_one(
        {"name": "Product 1"},
        {"$set": {"quantity": 25, "available": True}},
    )

    updated_product = collection.find_one({"name": "Product 1"}, {"_id": 0})
    print("\nUpdated Product 1:")
    print(updated_product)

    client.close()


if __name__ == "__main__":
    main()
