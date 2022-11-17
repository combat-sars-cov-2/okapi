import click

from workbench.src.lib.install import commands as installers
from workbench.src.lib.manage import commands as services
from workbench.src.lib.build import commands as builders

__version__ = "0.0.1"


@click.group(context_settings={"help_option_names": ("-h", "--help")})
@click.version_option(__version__, "--version", "-v")
@click.pass_context
def main(ctx):
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
main.add_command(builders.build)
