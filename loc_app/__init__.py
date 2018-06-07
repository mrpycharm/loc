# --- python imports
import motor
from urllib.parse import quote

# --- app module import
from loc_app.config.db_config import DB_USER, DB_PASS, DB_URL, DB_DB


# generate a motor client
client = motor.motor_tornado.MotorClient('mongodb://' + DB_USER + ':' + quote(DB_PASS) + '@' + DB_URL + '/' + DB_DB)

# get the db
db = client[DB_DB]
