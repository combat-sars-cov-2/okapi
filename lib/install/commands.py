import click

from lib.install.galaxy import commands as galaxy
from lib.install.irida import commands as irida


@click.group()
def install():
    """SARS-COV-2 Workbench (irida, galaxy ) utility scripts.
    Group of commands to install and uninstall
    workbench tools, plugins, workflows.

    support@sanbi.ac.za - for any issues
    \f
    """
    pass


install.add_command(irida.irida_plugins)
install.add_command(galaxy.galaxy_tools)
install.add_command(galaxy.singularity_images)
install.add_command(galaxy.pangolin)
install.add_command(galaxy.nanopore)
