from __future__ import annotations

import click
import os
from pathlib import Path
from decouple import config
from .share import *
from src.sanbi_sars_cov_workbench.lib.utils.helpers.ssh import SshSession
from src.sanbi_sars_cov_workbench.lib.utils.tools import read_from_plugins, install_gx_tools

CURRENT_DIR = os.path.dirname(__file__)
PATH_TO_PLUGINS = os.path.join(CURRENT_DIR, f"artifacts/plugins")


@click.command()
@click.option(
    "-c",
    "--conf",
    type=click.Path(exists=True),
    help=f"Location of the client config files (default={Path.home()}/.workbench.yaml)",
)
def irida_plugins(conf):
    # @TODO: restart irida
    ssh = SshSession(conf)
    config, ssh_session = ssh.get_ssh_session()
    download_jar(config, ssh_session)
    deploy_to_irida(config, ssh_session)
@click.command()
@click.option(
    "--galaxy", default="http://my.workbench.org:90", help="The targeted Galaxy instance"
)
@click.option(
    "--user",
    default="admin@galaxy.org",
    help="The username to use accessing the galaxy instance",
)
@click.option("--password", default="password", help="Password for the user")
@click.option(
    "--api-key", default="fakekey", help="API Key token generated for the user"
)
def galaxy_tools(galaxy, user, password, api_key):
    """
    This command installs the tools in galaxy
    """
    logger.info("Install to Galaxy Instance")
    plugins_tools = read_from_plugins(PATH_TO_PLUGINS)
    install_gx_tools(plugins_tools)

@click.group()
def install():
    """
    Group of sub-commands to install sanbi_sars_cov_workbench tools, plugins, workflows.
    \f
    """
    pass


install.add_command(irida_plugins)
install.add_command(galaxy_tools)

# For Deploy
# install.add_command(galaxy.singularity_images)
