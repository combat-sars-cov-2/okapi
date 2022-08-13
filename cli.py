from pathlib import Path

import click

from lib.install import commands as installers
from lib.start import commands as services


@click.group()
@click.option("--config", type=str, help=f"Location of the client config files (default={Path.home()}/.workbench)")
@click.option("-D", "--debug", is_flag=True, default=False, help="Enable debug mode")
@click.option("-H", "--host", type=list, help="Socket(s) address for instances targeted")
@click.option("-v", "--version", help="Print version information and quit")
@click.pass_context
def workbench(ctx, config, debug, host, version):
    """SARS-COV-2 Workbench (irida, galaxy ) utility scripts.
    Group of utility commands
    to manage the workbench_cli.

    support@sanbi.ac.za - for any issues
    \f
    """
    ctx.ensure_object(dict)
    ctx.obj['host_list'] = host
    pass


workbench.add_command(installers.install)
workbench.add_command(services.start)
