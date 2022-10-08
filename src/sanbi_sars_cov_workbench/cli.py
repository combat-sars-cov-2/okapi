import click

from src.sanbi_sars_cov_workbench.lib.install import commands as installers
from src.sanbi_sars_cov_workbench.lib.manage import commands as services


@click.group()
@click.option("--version", help="Print version information and quit")
def main(version):
    """SARS-COV-2 Workbench (irida_workbench, galaxy_workbench ) utility scripts.
    Group of utility commands
    to manage the workbench_cli.

    support@sanbi.ac.za - for any issues
    \f
    """
    pass


main.add_command(services.start)
main.add_command(services.stop)
main.add_command(installers.install)
