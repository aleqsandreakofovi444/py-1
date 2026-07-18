from pymongo import MongoClient
import mongomock

from app.config import Config


class MovieRepository:
    def __init__(self):
        self.client = self._build_client()
        self.db = self.client[Config.MONGODB_DB]
        self.collection = self.db[Config.MONGODB_COLLECTION]
        self._seed_if_needed()

    def _build_client(self):
        try:
            client = MongoClient(Config.MONGODB_URI, serverSelectionTimeoutMS=2000)
            client.admin.command("ping")
            return client
        except Exception:
            return mongomock.MongoClient()

    def _seed_if_needed(self):
        if self.collection.count_documents({}) > 0:
            return

        movies = [
            {"title": "Inception", "year": 2010, "rating": 8.8, "genre": "Sci-Fi", "duration": 148},
            {"title": "The Matrix", "year": 1999, "rating": 8.7, "genre": "Action", "duration": 136},
            {"title": "Interstellar", "year": 2014, "rating": 8.6, "genre": "Sci-Fi", "duration": 169},
            {"title": "The Godfather", "year": 1972, "rating": 9.2, "genre": "Crime", "duration": 175},
            {"title": "Pulp Fiction", "year": 1994, "rating": 8.9, "genre": "Crime", "duration": 154},
            {"title": "The Dark Knight", "year": 2008, "rating": 9.0, "genre": "Action", "duration": 152},
            {"title": "The Matrix", "year": 1999, "rating": 8.7, "genre": "Sci-Fi", "duration": 136},
            {"title": "Interstellar", "year": 2014, "rating": 8.6, "genre": "Sci-Fi", "duration": 169},
            {"title": "The Dark Knight", "year": 2008, "rating": 9.0, "genre": "Action", "duration": 152},
            {"title": "Fight Club", "year": 1999, "rating": 8.8, "genre": "Drama", "duration": 139},
            {"title": "Forrest Gump", "year": 1994, "rating": 8.8, "genre": "Drama", "duration": 142},
            {"title": "Gladiator", "year": 2000, "rating": 8.5, "genre": "Action", "duration": 155},
            {"title": "The Shawshank Redemption", "year": 1994, "rating": 9.3, "genre": "Drama", "duration": 142},
            {"title": "The Prestige", "year": 2006, "rating": 8.5, "genre": "Drama", "duration": 130},
            {"title": "Avatar", "year": 2009, "rating": 7.8, "genre": "Sci-Fi", "duration": 162},
            {"title": "Whiplash", "year": 2014, "rating": 8.5, "genre": "Drama", "duration": 106},
            {"title": "Joker", "year": 2019, "rating": 8.4, "genre": "Drama", "duration": 122},
            {"title": "Parasite", "year": 2019, "rating": 8.5, "genre": "Thriller", "duration": 132},
            {"title": "The Wolf of Wall Street", "year": 2013, "rating": 8.2, "genre": "Biography", "duration": 180},
            {"title": "Mad Max: Fury Road", "year": 2015, "rating": 8.1, "genre": "Action", "duration": 120},
            {"title": "Django Unchained", "year": 2012, "rating": 8.4, "genre": "Western", "duration": 165},
        ]
        self.collection.insert_many(movies)

    def get_all_movies(self):
        return list(self.collection.find().sort("year", 1))

    def get_movie_count(self):
        return self.collection.count_documents({})

    def get_average_duration(self):
        result = self.collection.aggregate([
            {"$group": {"_id": None, "average_duration": {"$avg": "$duration"}}}
        ])
        values = list(result)
        if not values:
            return 0
        return round(values[0]["average_duration"], 2)
