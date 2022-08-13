import click
from github import Github, GithubException
from loguru import logger

from lib.utils.helper import download_plugin_assets, extract_plugin_jars


@click.group()
def irida():
    """SARS-COV-2 Workbench (irida, galaxy ) utility scripts.
    Group of commands to manage an irida instance for the workbench.
    """
    pass


@irida.command()
@click.option("--illumina-version", default="latest", help="Illumina (SARS-COV-2) release version")
@click.option("--nanopore-version", default="latest", help="Nanopore (SARS-COV-2) release version")
def plugins(illumina_version, nanopore_version):
    """
    This command downloads the plugins (jar) from github and installs them to irida instance
    :param illumina_version:  A version of the illumina plugin
    :param nanopore_version: A version of the nanopore plugin
    :return:  installation_status
    """
    try:
        g = Github(None)
    except GithubException as e:
        logger.error("Github token is invalid")
        raise click.ClickException(f"Something went wrong: {repr(e)}")

    plugin_versions = {"irida-plugin-sars-cov-2-illumina": illumina_version,
                       "irida-plugin-sars-cov-2-nanopore": nanopore_version}

    # downloads the plugin jars
    download_plugin_assets(g, plugin_versions)

    # extract the compressed plugins (jar)
    extract_plugin_jars()

    # install the plugin jars
