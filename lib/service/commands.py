import click

from lib.install.galaxy import commands as galaxy
from lib.install.irida import commands as irida


@click.group()
def service():
    """SARS-COV-2 Workbench (irida, galaxy ) utility scripts.
    Group of commands to service various servers between
    galaxy and irida.

    support@sanbi.ac.za - for any issues
    \f
    """
    pass


service.add_command(irida.irida_plugins)
service.add_command(galaxy.galaxy_tools)
service.add_command(galaxy.singularity_images)
