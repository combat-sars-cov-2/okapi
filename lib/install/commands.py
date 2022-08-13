import click

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


install.add_command(irida.plugins)
