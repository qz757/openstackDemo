from pecan import rest
from wsme import types as wtypes

from openstackDemo.api import expose
from openstackDemo.api.controllers.v1.users import UsersController as users_controller

class V1Controller(rest.RestController):
    users = users_controller()
    @expose.expose(wtypes.text)
    def get(self):
        return 'openstackDemo v1controller'
