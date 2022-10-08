from src.sanbi_sars_cov_workbench.lib.utils.services.factory import (
    ServiceFactory,
)


class IridaService(ServiceFactory):
    """
    Irida class - a representative of Irida server object
    """

    def __init__(self, api_key, secret):
        self._key = api_key
        self._secret = secret

    def test_connection(self):
        """
        TODO:
        Test through the api if connection is possible
        If the connection is ok, a relaunch of the services is done via api if possible.
        """
        pass

    def soft_launch(self):
        """
        TODO:
        Launch irida_workbench via api if connection fails
        If this is successful a code is returned and relaunching/launching irida_workbench via docker is skipped
        """
        pass


class IridaServiceBuilder:
    def __init__(self):
        self._instance = None

    def __call__(self, api_client_key, api_client_secret, **_ignored):
        if not self._instance:
            api_key, secret = self.authorize(api_client_key, api_client_secret)
            self._instance = IridaService(api_key, secret)
        return self._instance

    @staticmethod
    def authorize(key, secret):
        return "IRIDA_KEY", "IRIDA_SECRET"


factory = ServiceFactory()
factory.register_builder("IRIDA", IridaServiceBuilder())
