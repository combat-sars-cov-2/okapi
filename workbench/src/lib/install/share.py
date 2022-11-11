import click
import os
import fnmatch
import subprocess

from github import Github, GithubException
from loguru import logger

from workbench.src.lib.utils.helpers.misc import (
    download_plugin_assets,
    extract_plugin_jars,
)
from workbench.src.definitions import PROJECT_PATH_TO_PLUGINS


def pre_download_requirements(config):
    try:
        g = Github(None)
    except GithubException as e:
        logger.error("Github token is invalid")
        raise click.ClickException(f"Something went wrong: {repr(e)}")

    plugin_versions = {
        "irida-plugin-sars-cov-2-illumina": config["workflows"]["illumina_version"],
        "irida-plugin-sars-cov-2-nanopore": config["workflows"]["nanopore_version"],
    }
    return g, plugin_versions


def download_jar(config, ssh_session):
    """
    This command downloads the workbench plugins from github
    Note: Default version is latest package release
    """
    g, plugin_versions = pre_download_requirements()
    download_plugin_assets(g, plugin_versions)
    extract_plugin_jars()
    deploy_to_irida(config, ssh_session)


def deploy_to_irida(config, ssh_session):
    """
    Copy the irida jar plugins to the irida instance
    @return:
    """
    files = fnmatch.filter(os.listdir(PROJECT_PATH_TO_PLUGINS), "*.jar")
    ssh_session.bulk_upload(files, config["workflows"]["location_paths"])
