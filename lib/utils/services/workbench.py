from lib.utils.services.factory import ServiceFactory
from lib.utils.services.galaxy import GalaxyServiceBuilder
from lib.utils.services.irida import IridaServiceBuilder

factory = ServiceFactory()
factory.register_builder("IRIDA", IridaServiceBuilder())
factory.register_builder("GALAXY", GalaxyServiceBuilder())
