import pdb
from pathlib import Path

import click
import yaml

from lib.install import commands as installers
from lib.start import commands as services


@click.command()
@click.option("--debug/--no-debug", is_flag=True, default=False, help="Enable debug mode")
@click.option("--version", help="Print version information and quit")
@click.option('--conf', type=click.Path(exists=True),
              help=f"Location of the client config files (default={Path.home()}/.workbench.yaml)")
@click.pass_context
def workbench(ctx, debug, conf, version):
    """SARS-COV-2 Workbench (irida, galaxy ) utility scripts.
    Group of utility commands
    to manage the workbench_cli.

    support@sanbi.ac.za - for any issues
    \f
    """
    pdb.set_trace()
    cfg = read_config_file(conf)
    ctx.ensure_object(dict)
    # ctx.obj['host_list'] =


def read_config_file(conf):
    """
    READ the config file
    :param config: a configuration file
    :return: dict of config items
    """
    with open(conf, "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)


workbench.add_command(installers.install)
workbench.add_command(services.start)
