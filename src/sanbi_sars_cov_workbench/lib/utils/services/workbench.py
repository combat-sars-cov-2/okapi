from src.sanbi_sars_cov_workbench.lib.utils.services.factory import (
    ServiceFactory,
)
from src.sanbi_sars_cov_workbench.lib.utils.services.galaxy import (
    GalaxyServiceBuilder,
)
from src.sanbi_sars_cov_workbench.lib.utils.services.irida import (
    IridaServiceBuilder,
)

factory = ServiceFactory()
factory.register_builder("IRIDA", IridaServiceBuilder())
factory.register_builder("GALAXY", GalaxyServiceBuilder())
