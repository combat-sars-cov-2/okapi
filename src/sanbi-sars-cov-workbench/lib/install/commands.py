import click

from lib.install.galaxy import commands as galaxy
from lib.install.irida import commands as irida


@click.group()
def install():
    """
    Group of sub-commands to install sanbi-sars-cov-workbench tools, plugins, workflows.
    \f
    """
    pass


install.add_command(irida.irida_plugins)
install.add_command(galaxy.galaxy_tools)
install.add_command(galaxy.singularity_images)
install.add_command(galaxy.pangolin)
install.add_command(galaxy.nanopore)
