from __future__ import annotations

import click

from pathlib import Path
from workbench.src.lib.utils.helpers.ssh import SshSession

CONFIG_DEFAULTS = {"file": f"{Path.home()}/.workbench.yaml"}


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
    help=f"Location of the client config files (default={Path.home()}/.workbench.yaml)",
)
def start(conf):
    """
    Start up all the workbench components (docker containers)
    \f
    """
    ssh = SshSession(conf)
    config, ssh_session = ssh.get_ssh_session()
    start_up(config["workbench"], ssh_session)


@click.command()
@click.option(
    "-c",
    "--conf",
    type=click.Path(exists=True),
    help=f"Location of the client config files (default={Path.home()}/.workbench.yaml)",
)
def stop(conf):
    """
    Stop all the workbench components (docker containers)
    \f
    """
    ssh = SshSession(conf)
    config, ssh_session = ssh.get_ssh_session()
    shut_all(config["workbench"], ssh_session)
