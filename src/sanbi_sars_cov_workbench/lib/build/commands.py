from __future__ import annotations

import click
import os

from github import Github, GithubException
from loguru import logger

from pathlib import Path
from src.sanbi_sars_cov_workbench.lib.utils.helpers.ssh import SshSession
from src.sanbi_sars_cov_workbench.lib.utils.tools import read_from_plugins
from src.sanbi_sars_cov_workbench.lib.utils.helpers.misc import download_plugin_assets, extract_plugin_jars
from src.sanbi_sars_cov_workbench.lib.utils.tool_shed import complete_metadata
from src.sanbi_sars_cov_workbench.definitions import PROJECT_PATH_TO_PLUGINS


@click.command()
@click.option("--illumina-version", default="latest", help="Illumina (SARS-COV-2) release version")
@click.option("--nanopore-version", default="latest", help="Nanopore (SARS-COV-2) release version")
@click.option("--access-token", help="Your unexpired & valid github access token")
def singularity_images(illumina_version, nanopore_version, access_token):
    """
    Build Singularity Images from a Galaxy Workflow file.
    :return: status
    """
    try:
        g = Github(access_token)
    except GithubException as e:
        logger.error("Github token is missing or invalid")
        raise click.ClickException(f"Something went wrong: {repr(e)}")

    plugin_versions = {
        "irida-plugin-sars-cov-2-illumina": illumina_version,
        "irida-plugin-sars-cov-2-nanopore": nanopore_version,
    }
    # download plugins
    download_plugin_assets(g, plugin_versions)

    # unpack the jar files
    extract_plugin_jars()

    tool_list = read_from_plugins(PROJECT_PATH_TO_PLUGINS)
    for tools in tool_list:
        for t in tools:
            try:
                data = complete_metadata(t)
                print(data)
            except Exception as e:
                logger.error(f"Error, while trying to build image for tool {t['name']}")
                raise click.ClickException(f"Something went wrong: {repr(e)}")


@click.group()
def build():
    """
    Group of sub-commands to install sanbi_sars_cov_workbench tools, plugins, workflows.
    \f
    """
    pass


build.add_command(singularity_images)
