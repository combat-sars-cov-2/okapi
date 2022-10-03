from __future__ import annotations

from pathlib import Path

import click

from loguru import logger
from src.sanbi_sars_cov_workbench.lib.shared.galaxy import launch as galaxy_launch
from src.sanbi_sars_cov_workbench.lib.shared.irida import launch as irida_launch
from src.sanbi_sars_cov_workbench.lib.utils.helpers.misc import read_config_file
from src.sanbi_sars_cov_workbench.lib.utils.helpers.ssh import SshBasic, SshKeyBase
from src.sanbi_sars_cov_workbench.lib.utils.services.galaxy import factory as galaxy_factory
from src.sanbi_sars_cov_workbench.lib.utils.services.irida import factory as irida_factory

CONFIG_DEFAULTS = {"file": f"{Path.home()}/.okapi.yaml"}


def launch_all(cfg, ssh_session):
    """
    Using
    :return:
    """
    cmd = f"cd {cfg['root_path']};"
    cmd += (
        "docker-compose -f docker-compose.yml -f docker-compose.singularity.yml -f docker-compose.irida_workbench.yml -f "
        "docker-compose.irida_ssl.yml up -d "
    )
    ssh_session.exec(cmd)


def shut_all(cfg, ssh_session):
    """
    Using
    :return:
    """
    cmd = f"cd {cfg['root_path']};"
    cmd += (
        "docker-compose -f docker-compose.yml -f docker-compose.singularity.yml -f docker-compose.irida_workbench.yml -f "
        "docker-compose.irida_ssl.yml down "
    )
    ssh_session.exec(cmd)


FUNC_MAP = {"all": launch_all, "irida_workbench": irida_launch, "galaxy_workbench": galaxy_launch}


@click.command()
@click.option(
    "-c",
    "--conf",
    type=click.Path(exists=True),
    help=f"Location of the client config files (default={Path.home()}/.okapi.yaml)",
)
@click.argument(
    "instance", type=click.Choice(["all", "irida_workbench", "galaxy_workbench"]), required=True
)
def launch(instance, conf):
    """
    Launch a service of the sanbi_sars_cov_workbench
    \f
    """
    cfg = read_config_file(conf) if conf else read_config_file(CONFIG_DEFAULTS["file"])

    logger.info("Checking if the irida_workbench is up already through their API")
    irida = irida_factory.create("IRIDA", **cfg["irida_workbench"])
    irida.test_connection()

    logger.info("Checking if the galaxy_workbench is up already through their API")
    galaxy = galaxy_factory.create("GALAXY", **cfg["galaxy_workbench"])
    galaxy.test_connection()

    func = FUNC_MAP[instance]
    ssh_session = (
        SshBasic(cfg[instance])
        if cfg["auth"]["basic_auth"]
        else SshKeyBase(cfg[instance])
    )

    func(cfg, ssh_session)
