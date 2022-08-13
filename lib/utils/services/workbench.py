from lib.utils.services.factory import ServiceFactory


class WorkbenchService(ServiceFactory):
    """
    Workbench class - a representative of a Workbench server object
    """

    def __init__(self, api_key, secret):
        self._key = api_key
        self._secret = secret

    def test_connection(self):
        print(f'Accessing Workbench with {self._key} and {self._secret}')

    def start(self):
        print(f'Starting Workbench with {self._key} and {self._secret}')


class WorkbenchServiceBuilder:
    def __init__(self):
        self._instance = None

    def __call__(self, workbench_client_key, workbench_client_secret, **_ignored):
        if not self._instance:
            api_key, secret = self.authorize(workbench_client_key, workbench_client_secret)
            self._instance = WorkbenchService(api_key, secret)
        return self._instance

    def authorize(self, key, secret):
        # test the ssh connection before proceeding
        return 'GALAXY_KEY', 'GALAXY_SECRET'


factory = ServiceFactory()
factory.register_builder('GALAXY', WorkbenchServiceBuilder())
