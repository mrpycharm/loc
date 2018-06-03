# --- python imports
from tornado.gen import coroutine

# --- app module imports
from loc_app import db
from loc_app.helpers.utils import log

@coroutine
def database_read_one(collection, read_filter={}, result_filter={}):
    results = None
    if db:
        db_collection = db[collection]
        if not db_collection:
            db_collection = yield db.create_collection(collection)

        results = yield db_collection.find_one(read_filter, result_filter)
        log(results)

    return results


@coroutine
def database_read_many(collection, read_filter={}, result_filter={}):
    results = None
    if db:
        db_collection = db[collection]
        if not db_collection:
            db_collection = yield db.create_collection(collection)

        results = yield db_collection.find(read_filter, result_filter)
        log(results)

    return results
    