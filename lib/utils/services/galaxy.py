from lib.utils.services.factory import ServiceFactory


class GalaxyService(ServiceFactory):
    """
    Galaxy class - a representative of a Galaxy server object
    """

    def __init__(self, api_key, secret):
        self._key = api_key
        self._secret = secret

    def test_connection(self):
        pass

    def start(self):
        pass


class GalaxyServiceBuilder:
    def __init__(self):
        self._instance = None

    def __call__(self, client_key, client_secret, **_ignored):
        if not self._instance:
            api_key, secret = self.authorize(client_key, client_secret)
            self._instance = GalaxyService(api_key, secret)
        return self._instance

    @staticmethod
    def authorize(key, secret):
        return 'GALAXY_KEY', 'GALAXY_SECRET'


factory = ServiceFactory()
factory.register_builder('GALAXY', GalaxyServiceBuilder())
