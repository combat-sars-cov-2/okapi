import os
import subprocess
import sys

import click
from loguru import logger

# from toolshed import complete_metadata

this = sys.modules[__name__]


def build_image(tool_spec_str):
    tools = tool_spec_str[0].split(",")
    for tool in tools:
        try:
            command = f'mulled-build build-and-test --test echo --singularity "{tool}"'
            process = subprocess.Popen(command, shell=True)
            # with process.stdout:
            #     logger.info(process.stdout)
            status = os.waitpid(process.pid, 0)[1]
        except Exception as e:
            logger.error(f"Error, while trying building the image {tool_spec_str}")
            raise click.ClickException(f"Something went wrong: {repr(e)}")


def move_images(src, dest):
    try:
        command = f'cp -R "{src}" "{dest}"'
        process = subprocess.Popen(command, shell=True)
        status = os.waitpid(process.pid, 0)[1]
    except Exception as e:
        logger.error(f"Error, while trying to move images from {src} to {dest}")
        raise click.ClickException(f"Something went wrong: {repr(e)}")


def list_images():
    pass
