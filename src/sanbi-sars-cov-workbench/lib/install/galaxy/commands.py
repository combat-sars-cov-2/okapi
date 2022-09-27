import os

import click
from github import Github, GithubException
from loguru import logger

from lib.utils.helpers.misc import download_plugin_assets, extract_plugin_jars
from lib.utils.tool_shed import complete_metadata
from lib.utils.tools import read_from_plugins, install_gx_tools

CURRENT_DIR = os.path.dirname(__file__)
PATH_TO_PLUGINS = os.path.join(CURRENT_DIR, f"sources/plugins/")


@click.command()
@click.option(
    "--galaxy-workbench", default="http://nginx:90", help="The targeted Galaxy instance"
)
@click.option(
    "--user",
    default="admin@galaxy-workbench.org",
    help="The username to use accessing the galaxy-workbench instance",
)
@click.option("--password", default="password", help="Password for the user")
@click.option(
    "--api-key", default="fakekey", help="API Key token generated for the user"
)
def galaxy_tools(galaxy, user, password, api_key):
    """
    This command installs the workflow in Galaxy
    """
    logger.info("Install to Galaxy Instance")
    plugins_tools = read_from_plugins(PATH_TO_PLUGINS)
    install_gx_tools(plugins_tools)


@click.command()
@click.option(
    "--illumina-version", default="latest", help="Illumina (SARS-COV-2) release version"
)
@click.option(
    "--nanopore-version", default="latest", help="Nanopore (SARS-COV-2) release version"
)
def singularity_images(illumina_version, nanopore_version):
    """
    Build Singularity Images from a Galaxy Workflow file
    :return: status
    """
    try:
        g = Github(None)
    except GithubException as e:
        logger.error("Github token is missing or invalid")
        raise click.ClickException(f"Something went wrong: {repr(e)}")

    plugin_versions = {
        "irida-workbench-plugin-sars-cov-2-illumina": illumina_version,
        "irida-workbench-plugin-sars-cov-2-nanopore": nanopore_version,
    }
    # download plugins
    download_plugin_assets(g, plugin_versions)

    # unpack the jar files
    extract_plugin_jars()

    tool_list = read_from_plugins(PATH_TO_PLUGINS)
    for tools in tool_list:
        for t in tools:
            try:
                data = complete_metadata(t)
                print(data)
            except Exception as e:
                logger.error(f"Error, while trying to build image for tool {t['name']}")
                raise click.ClickException(f"Something went wrong: {repr(e)}")


@click.command()
def pangolin():
    """
    This command installs the pangolin tool in galaxy-workbench
    """
    pass


@click.command()
def nanopore():
    """
    This command installs the nanopore tool in galaxy-workbench
    """
    pass
