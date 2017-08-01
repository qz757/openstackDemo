from pecan import rest
from wsme import types as wtypes

from openstackDemo.api import expose

from openstackDemo.api.controllers.v1 import controller as v1_controller

class RootController(rest.RestController):
    v1 = v1_controller.V1Controller()

    @expose.expose(wtypes.text)
    def get(self):
        return "openstackDemoJson"
