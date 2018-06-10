# --- python imports
from tornado.gen import coroutine

# --- app module imports
from loc_app import db
from loc_app.helpers.utils import log

@coroutine
def database_read_one(collection, read_filter={}, result_filter=None):
    results = None
    if db:
        db_collection = db[collection]
        if not db_collection:
            db_collection = yield db.create_collection(collection)

        if read_filter:
            results = yield db_collection.find_one(read_filter, result_filter)
        else:
            results = yield db_collection.find_one(read_filter)

    return results


@coroutine
def database_read_many(collection, read_filter={}, result_filter=None):
    results = None
    if db:
        db_collection = db[collection]
        if not db_collection:
            db_collection = yield db.create_collection(collection)

        if result_filter:
            cursor = db_collection.find(read_filter, result_filter)
            results = yield cursor.to_list(None)

        else:
            cursor = db_collection.find(read_filter)
            results = yield cursor.to_list(None)

    return results


@coroutine
def database_insert_one(collection, data):
    if db:
        db_collection = db[collection]
        if not db_collection:
            db_collection = yield db.create_collection(collection)

        results = yield db_collection.insert_one(data)
        log(results)

        try:
            data.pop('_id')
        except:
            pass


@coroutine
def database_insert_many(collection, data, ordered=True):
    if db:
        db_collection = db[collection]
        if not db_collection:
            db_collection = yield db.create_collection(collection)

        if isinstance(data, list):
            results = yield db_collection.insert_many(data, ordered=ordered)
            log(results)

            for doc in data:
                try:
                    doc.pop('_id')
                except:
                    pass


@coroutine
def database_update(collection, read_filter, update, multi=False):
    results = None
    if db:
        db_collection = db[collection]
        if not db_collection:
            db_collection = yield db.create_collection(collection)

        if not multi:
            results = yield db_collection.update_one(read_filter, update)
        else:
            results = yield db_collection.update_many(read_filter, update)


@coroutine
def database_delete(collection, read_filter, multi=False):
    results = None
    if db:
        db_collection = db[collection]
        if not db_collection:
            db_collection = yield db.create_collection(collection)

        if not multi:
            results = yield db_collection.delete_one(read_filter)
        else:
            results = yield db_collection.delete_many(read_filter)
        log(results)