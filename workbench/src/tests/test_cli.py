"""
Tests for command line interface (CLI)
"""
from importlib.metadata import version
from os import linesep

from workbench.src import cli

from click.testing import CliRunner

from cli_test_helpers import shell


def test_runas_module():
    """
    Can this package be run as a Python module?
    """
    result = shell("python -m workbench.src.cli --help")
    assert result.exit_code == 0


def test_entrypoint():
    """
    Is entrypoint script installed? (setup.py)
    """
    result = shell("workbench --help")
    assert result.exit_code == 0


def test_version_command():
    """
    Does --version display information as expected?
    """
    # expected_version = version("workbench -v")
    expected_version = cli.__version__
    result = shell("workbench --version")

    assert result.stdout == f"workbench, version {expected_version}{linesep}"
    assert result.exit_code == 0


def test_example_command():
    """
    Is command available?
    """
    result = shell("workbench start --help")
    assert result.exit_code == 0


# NOTE:
# You can continue here, adding all CLI command combinations
# using a non-destructive option, such as --help, to test for
# the availability of the CLI command or option.


def test_cli():
    """
    Does CLI stop execution w/o a command argument?
    """
    runner = CliRunner()
    result = runner.invoke(cli.main)

    assert result.exit_code == 0
