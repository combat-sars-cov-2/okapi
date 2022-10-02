import os

import click
from decouple import config
from github import Github, GithubException
from loguru import logger

from lib.utils.helpers.misc import download_plugin_assets, extract_plugin_jars

CONTEXT_SETTINGS = dict(
    default_map={
        "download_jar": {
            "illumina_version": config("ILLUMINA_VERSION", default="latest"),
            "nanopore_version": config("NANOPORE_VERSION", default="latest"),
        }
    }
)

CURRENT_DIR = os.path.dirname(__file__)
PATH_TO_PLUGINS = os.path.join(CURRENT_DIR, f"sources/plugins/")


@click.command()
@click.option(
    "--illumina-version", default="latest", help="Illumina (SARS-COV-2) release version"
)
@click.option(
    "--nanopore-version", default="latest", help="Nanopore (SARS-COV-2) release version"
)
def irida_plugins(illumina_version, nanopore_version):
    """
    This command installs workflow plugins into IRIDA

    :param illumina_version:  A version of the illumina plugin
    :param nanopore_version: A version of the nanopore plugin
    :return:  installation_status
    """
    try:
        g = Github(None)
    except GithubException as e:
        logger.error("Github token is invalid")
        raise click.ClickException(f"Something went wrong: {repr(e)}")

    plugin_versions = {
        "irida-workbench-plugin-sars-cov-2-illumina": illumina_version,
        "irida-workbench-plugin-sars-cov-2-nanopore": nanopore_version,
    }

    # downloads the plugin jars
    download_plugin_assets(g, plugin_versions)

    # extract the compressed plugins (jar) - to the relevant dir
    extract_plugin_jars()
