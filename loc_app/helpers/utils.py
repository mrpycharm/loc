# --- app module imports
from loc_app.config.app_config import LOGGING


def log(statment):
    if LOGGING:
        print(statment)
