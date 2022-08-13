import click

from lib.install import commands as installers


@click.group()
def workbench():
    """SARS-COV-2 Workbench (irida, galaxy ) utility scripts.
    Group of utility commands
    to manage the workbench_cli.

    support@sanbi.ac.za - for any issues
    \f
    """
    pass


workbench.add_command(installers.install)
