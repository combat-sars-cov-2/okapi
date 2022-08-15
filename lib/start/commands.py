from __future__ import annotations

import click

from lib.utils.services.galaxy import factory as galaxy_factory

config = {
    'galaxy_client_key': 'THE_GALAXY_CLIENT_KEY',
    'galaxy_client_secret': 'THE_GALAXY_CLIENT_SECRET',
}


@click.command()
@click.option('-i', '--instance', type=click.Choice(['workbench', 'irida', 'galaxy']), required=True)
def start(instance):
    """
    Start a service of the workbench
    \f
    """
    if instance == 'workbench':
        pandora = galaxy_factory.create('WORKBENCH', **config)
        pandora.test_connection()

    if instance == 'irida':
        galaxy = galaxy_factory.create('IRIDA', **config)
        galaxy.test_connection()

    if instance == 'galaxy':
        local = galaxy_factory.create('GALAXY', **config)
        local.start()
