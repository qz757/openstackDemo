from wsme import types as wtypes
from pecan import rest
from openstackDemo.api import expose
from wsme import types as wtypes
import pecan


class User(wtypes.Base):
    id = wtypes.wsattr(wtypes.text, mandatory=True)
    name = wtypes.text
    age = int


class Users(wtypes.Base):
    users = [User]

class UserController(rest.RestController):

    def __init__(self, user_id):
        self.user_id = user_id

    @expose.expose(User)
    def get(self):
        user_info = {
            'id': self.user_id,
            'name': 'Alice',
            'age': 30,
        }
        return User(**user_info)

class UsersController(rest.RestController):

    @pecan.expose()
    def _lookup(self, user_id, *remainder):
        return UserController(user_id), remainder
