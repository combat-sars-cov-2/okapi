from __future__ import annotations

from pathlib import Path

import click

from src.sanbi_sars_cov_workbench.lib.utils.helpers.misc import read_config_file
from src.sanbi_sars_cov_workbench.lib.utils.helpers.ssh import SshBasic, SshKeyBase

CONFIG_DEFAULTS = {"file": f"{Path.home()}/.okapi.yaml"}


def start_up(cfg, ssh_session):
    """
    Using
    :return:
    """
    cmd = f"cd {cfg['root_path']};"
    cmd += (
        "docker-compose -f docker-compose.yml -f docker-compose.singularity.yml -f docker-compose.irida.yml "
        "-f "
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
        "docker-compose -f docker-compose.yml -f docker-compose.singularity.yml -f docker-compose.irida.yml "
        "-f "
        "docker-compose.irida_ssl.yml down "
    )
    ssh_session.exec(cmd)


@click.command()
@click.option(
    "-c",
    "--conf",
    type=click.Path(exists=True),
    help=f"Location of the client config files (default={Path.home()}/.okapi.yaml)",
)
def start(conf):
    """
    Start up all the workbench components (docker containers)
    \f
    """
    cfg = read_config_file(conf) if conf else read_config_file(CONFIG_DEFAULTS["file"])

    ssh_session = (
        SshBasic(cfg['workbench'])
        if cfg["auth"]["basic_auth"]
        else SshKeyBase(cfg['workbench'])
    )
    ssh_session.connect()
    start_up(cfg['workbench'], ssh_session)


@click.command()
@click.option(
    "-c",
    "--conf",
    type=click.Path(exists=True),
    help=f"Location of the client config files (default={Path.home()}/.okapi.yaml)",
)
def stop(conf):
    """
    Stop all the workbench components (docker containers)
    \f
    """
    cfg = read_config_file(conf) if conf else read_config_file(CONFIG_DEFAULTS["file"])

    ssh_session = (
        SshBasic(cfg['workbench'])
        if cfg["auth"]["basic_auth"]
        else SshKeyBase(cfg['workbench'])
    )
    ssh_session.connect()
    shut_all(cfg['workbench'], ssh_session)
