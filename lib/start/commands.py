from __future__ import annotations

from pathlib import Path

import click
from loguru import logger

from lib.utils.helpers.misc import read_config_file
from lib.utils.helpers.ssh import SshBasic, SshKeyBase
from lib.utils.services.galaxy import factory as galaxy_factory
from lib.utils.services.irida import factory as irida_factory

CONFIG_DEFAULTS = {
    'file': f"{Path.home()}/.okapi.yaml"
}


def start_galaxy(ssh_session):
    """
    :return:
    """
    logger.info("ABOUT TO START GALAXY")
    ssh_session.connect()

    results = ssh_session.exec('dig')
    logger.debug(results)


def start_irida(ssh_session):
    """
    :return:
    """
    logger.info("ABOUT TO START IRIDA")
    pass


def start_all():
    """
    :return:
    """
    cmd = 'docker-compose -f docker-compose.yml -f docker-compose.singularity.yml -f docker-compose.irida.yml -f ' \
          'docker-compose.irida_ssl.yml up -d '
    pass


FUNC_MAP = {
    'all': start_all,
    'irida': start_irida,
    'galaxy': start_galaxy
}


@click.command()
@click.option('-c', '--conf', type=click.Path(exists=True),
              help=f"Location of the client config files (default={Path.home()}/.okapi.yaml)")
@click.argument('instance', type=click.Choice(['all', 'irida', 'galaxy']), required=True)
def start(instance, conf):
    """
    Start a service of the workbench
    \f
    """
    cfg = read_config_file(conf) if conf else read_config_file(CONFIG_DEFAULTS['file'])

    logger.info("Checking if the irida is up already through their API")
    irida = irida_factory.create('IRIDA', **cfg['irida'])
    irida.test_connection()

    logger.info("Checking if the galaxy is up already through their API")
    galaxy = galaxy_factory.create('GALAXY', **cfg['galaxy'])
    galaxy.test_connection()

    func = FUNC_MAP[instance]
    ssh_session = SshBasic(cfg[instance]) if cfg['auth']['basic_auth'] else SshKeyBase(cfg[instance])
    func(ssh_session)
