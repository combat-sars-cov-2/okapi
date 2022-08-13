from lib.utils.services.factory import ServiceFactory


class GalaxyService(ServiceFactory):
    """
    Galaxy class - a representative of a Galaxy server object
    """

    def __init__(self, api_key, secret):
        self._key = api_key
        self._secret = secret

    def test_connection(self):
        print(f'Accessing Galaxy with {self._key} and {self._secret}')

    def start(self):
        print(f'Starting Galaxy with {self._key} and {self._secret}')


class GalaxyServiceBuilder:
    def __init__(self):
        self._instance = None

    def __call__(self, galaxy_client_key, galaxy_client_secret, **_ignored):
        if not self._instance:
            api_key, secret = self.authorize(galaxy_client_key, galaxy_client_secret)
            self._instance = GalaxyService(api_key, secret)
        return self._instance

    def authorize(self, key, secret):
        return 'GALAXY_KEY', 'GALAXY_SECRET'


factory = ServiceFactory()
factory.register_builder('GALAXY', GalaxyServiceBuilder())
