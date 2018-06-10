# --- python imports
import uuid, json, hashlib
from tornado.gen import coroutine

# --- app module imports
from loc_app.helpers.utils import posted, hash_password, log
from loc_app.helpers.auth import expects
from loc_app.helpers.errors import InvalidUsage
from loc_app.handlers.base_handler import BaseHandler
from loc_app.database.database import *

class SignupHandler(BaseHandler):
    
    @expects(['username', 'email', 'password'])
    @coroutine
    def post(self):
        data = posted(self)

        username = data['username']
        password = data['password']
        email = data['email']

        existing_user = yield database_read_one('user', {'$or' : [{'email' : email}, {'username' : username}]})
        
        if existing_user:
            if existing_user.get('email') == email:
                raise InvalidUsage(reason='Email already exists.', status_code=452)
            raise InvalidUsage(reason='Username already taken.', status_code=452)

        hashed_pass, salt = hash_password(password)
        user = yield self.create_user(username, email, hashed_pass, salt)

        self.write(json.dumps(user))


    @coroutine
    def create_user(self, username, email, password, pass_salt):
        user = {
            'id' : '{0}'.format(uuid.uuid4()),
            'email' : email,
            'username' : username,
            'password' : password,
            'pass_salt' : pass_salt,
            'token' : ''
        }

        yield database_insert_one('user', user)
        return user 


class LoginHandler(BaseHandler):

    @expects(['username', 'password'])
    @coroutine
    def post(self):
        data = posted(self)

        user = yield database_read_one('user', {'username' : data['username']})
        log(user)
        if not user:
            raise InvalidUsage(reason='Invalid username', status_code=452)
        
        match = self.match_password(data['password'], user['password'], user['pass_salt'])
        if not match:
            raise InvalidUsage(reason='Wrong password.', status_code=452)

        token = yield self.session(user['id'])
        response = {
            'token' : token
        }

        self.write(json.dumps(response))
        
        
    def match_password(self, pass_input, hashed_pass, salt):
        return hashlib.sha512((pass_input + salt).encode('UTF-8')).hexdigest() == hashed_pass

    @coroutine
    def session(self, uid):
        token = '{0}'.format(uuid.uuid4())
        yield database_update('user', {'id' : uid}, {'$set' : {'token' : token}})
        return token

        
