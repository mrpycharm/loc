# --- python imports
import uuid, json, hashlib, random, time
from tornado.gen import coroutine

# --- app module imports
from loc_app.helpers.utils import posted, hash_password, log
from loc_app.helpers.auth import expects
from loc_app.helpers.users import create_user
from loc_app.helpers.errors import InvalidUsage
from loc_app.handlers.base_handler import BaseHandler
from loc_app.database.database import *
from loc_app.config.app_config import OTP_EXPIRY

ONE_MINUTE = 60 # seconds

class GenerateOTPHandler(BaseHandler):

    @expects(['phone_number'])
    @coroutine
    def post(self):

        data = posted(self)
        phone_number = data['phone_number']
        log(type(phone_number))

        user = yield create_user(phone_number)
        otp, is_repeat = yield self.generate_otp(phone_number)
        if not is_repeat:
            # TODO: integrate SMS api
            log('OTP generate: ' + str(otp))

        response = {
            'status' : 'OK'
        }
        self.write(json.dumps(response))
        

    @coroutine
    def generate_otp(self, phone_number):

        code = ''.join([str(random.randrange(0, 9)) for i in range(6)])
        current_time = time.time()
        otp_expiry = current_time + (OTP_EXPIRY * ONE_MINUTE)
        is_repeat = False
        otp = yield database_read_one('otp', read_filter={'key' : phone_number})


        if not otp:
            otp = {
                'id' : '{0}'.format(uuid.uuid4()),
                'key' : phone_number,
                'otp' : code,
                'expires_at' : otp_expiry
            }
            yield database_insert_one('otp', otp)

        elif otp.get('expires_at') > current_time:
            is_repeat = True
            code = None
            return code, is_repeat

        else:
            yield database_update('otp', {'id' : otp['id']}, {'$set' : {'otp' : code, 'expires_at' : otp_expiry}})

        return code, is_repeat


class VerifyOTPHandler(BaseHandler):

    @expects(['phone_number', 'otp'])
    @coroutine
    def post(self):
        
        data = posted(self)
        phone_number = data['phone_number']
        otp = data['otp']

        success = yield self.verify_otp(phone_number, otp)
        if not success:
            raise InvalidUsage(reason='Invalid OTP.', status_code=452)

        yield self.set_user_verified(phone_number)

        response = {
            'status' : 'OK'
        }
        self.write(json.dumps(response))

    @coroutine
    def set_user_verified(self, phone_number):
        yield database_update('user', {'phone_number' : phone_number, 'mobile_verified' : False}, {'$set' : {'mobile_verified' : True}})


    @coroutine
    def verify_otp(self, phone_number, otp):
        
        current_time = time.time()
        otp = yield database_read_one('otp', read_filter={'key' : phone_number, 'otp' : otp, 'expires_at' : {'$gt' : current_time}})
        success = True if otp else False
        if success:
            yield database_delete('otp', {'key' : phone_number})

        return success