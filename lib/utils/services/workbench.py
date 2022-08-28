from lib.utils.services.factory import ServiceFactory
from lib.utils.services.galaxy import GalaxyServiceBuilder
from lib.utils.services.irida import IridaServiceBuilder

# class WorkbenchService(ServiceFactory):
#     """
#     Workbench class - a representative of a Workbench server object
#     """
#
#     def __init__(self, api_key, secret):
#         self._key = api_key
#         self._secret = secret
#
#     def test_connection(self, component):
#         """
#         TODO:
#         Test through the api if connection is possible both IRIDA & GALAXY
#         If the connection is ok, a restart of the services is done via api if possible.
#         """
#         print(f'Accessing {component} with {self._key} and {self._secret}')
#
#     def soft_start(self):
#         """
#         TODO:
#         Start irida via api if connection fails
#         If this is successful a code is returned and restarting/starting irida via docker is skipped
#         """
#         print(f"Soft starting workbench with {self._key} and {self._secret}")
#
#
# class WorkbenchServiceBuilder:
#     def __init__(self):
#         self._instance = None
#
#     def __call__(self, client_key, client_secret, **_ignored):
#         if not self._instance:
#             api_key, secret = self.authorize(client_key, client_secret)
#             self._instance = WorkbenchService(api_key, secret)
#         return self._instance
#
#     def authorize(self, key, secret):
#         # test the ssh connection before proceeding
#         return 'GALAXY_KEY', 'GALAXY_SECRET'

factory = ServiceFactory()
factory.register_builder('IRIDA', IridaServiceBuilder())
factory.register_builder('GALAXY', GalaxyServiceBuilder())
