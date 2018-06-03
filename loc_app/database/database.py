# --- python imports
import motor, urllib

# --- app module import
from loc_app.config.db_config import DB_USER, DB_PASS, DB_URL, DB_DB

# generate a motor client
client = motor.motor_tornado.MotorClient('mongodb://' + DB_USER + ':' + urllib.quote(DB_PASS) + '@' + DB_URL + '/' + DB_DB)
