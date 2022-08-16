from lib.utils.services.factory import ServiceFactory


class IridaService(ServiceFactory):
    """
    Irida class - a representative of a Irida server object
    """

    def __init__(self, api_key, secret):
        self._key = api_key
        self._secret = secret

    def test_connection(self):
        print(f'Accessing Irida with {self._key} and {self._secret}')

    def start(self):
        print(f'Starting Irida with {self._key} and {self._secret}')


class IridaServiceBuilder:
    def __init__(self):
        self._instance = None

    def __call__(self, irida_client_key, irida_client_secret, **_ignored):
        if not self._instance:
            api_key, secret = self.authorize(irida_client_key, irida_client_secret)
            self._instance = IridaService(api_key, secret)
        return self._instance

    def authorize(self, key, secret):
        return 'IRIDA_KEY', 'IRIDA_SECRET'


factory = ServiceFactory()
factory.register_builder('IRIDA', IridaServiceBuilder())
