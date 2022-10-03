import click

from lib.install import commands as installers
from lib.launch import commands as services


@click.group()
@click.option("--version", help="Print version information and quit")
def main(version):
    """SARS-COV-2 Workbench (irida-workbench, galaxy-workbench ) utility scripts.
    Group of utility commands
    to manage the workbench_cli.

    support@sanbi.ac.za - for any issues
    \f
    """
    pass


main.add_command(installers.install)
main.add_command(services.launch)
