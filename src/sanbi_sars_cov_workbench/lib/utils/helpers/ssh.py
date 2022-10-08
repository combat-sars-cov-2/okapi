import paramiko

from pathlib import Path
from loguru import logger
from typing import List
from src.sanbi_sars_cov_workbench.lib.utils.helpers.misc import read_config_file

# from paramiko.auth_handler import AuthenticationException, SSHException
from scp import SCPClient, SCPException

CONFIG_DEFAULTS = {"file": f"{Path.home()}/.workbench.yaml"}


class Ssh:
    """
    Class object to ssh to remote machine
    """

    def __init__(self, config):
        """
        Initialisation of the class attributes
        """
        self.username = config["user"]
        self.host = config["fqdn"]
        self.client = paramiko.client.SSHClient()

    def exec(self, cmd):
        """
        Execute a remote command
        :param cmd:
        :return:

        """
        logger.info(f"command: {cmd}")
        stdin, stdout, stderr = self.client.exec_command(cmd, get_pty=True)
        for line in iter(stdout.readline, ""):
            logger.debug(line, end="")
        logger.info("finished.")
        return stdout.read().decode()

    def bulk_upload(self, filepaths, remote_path):
        """
        Upload multiple files to a remote directory.

        :param List[str] filepaths: List of local files to be uploaded.
        """
        try:
            self.scp.put(filepaths, remote_path=remote_path, recursive=True)
            logger.info(
                f"Finished uploading {len(filepaths)} files to {remote_path} on {self.host}"
            )
        except SCPException as e:
            logger.error(f"SCPException during bulk upload: {e}")
        except Exception as e:
            logger.error(f"Unexpected exception during bulk upload: {e}")

    def close(self):
        """
        Close the ssh session
        :return:
        """
        self.client.close()

    @property
    def scp(self) -> SCPClient:
        conn = self.connection
        return SCPClient(conn.get_transport())


class SshBasic(Ssh):
    """
    Class object to SSH with username and password
    """

    def __init__(self, config):
        self.password = config["password"]
        super().__init__(config)

    def connect(self):
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(
            self.host,
            username=self.username,
            password=self.password,
            look_for_keys=False,
            allow_agent=False,
        )

    def exec(self, cmd):
        return super().exec(cmd)

    def bulk_upload(self, filepaths: List[str], remote_path):
        return super().bulk_upload(filepaths, remote_path)


class SshKeyBase(Ssh):
    """
    Class object to SSH with ssh key
    """

    def __init__(self, config):
        self.ssh_key = config["ssh_key"]
        super().__init__(config)

    def connect(self):
        """Connect with the ssh key"""
        pkey = paramiko.RSAKey.from_private_key_file(self.ssh_key)
        policy = paramiko.AutoAddPolicy()
        self.client.set_missing_host_key_policy(policy)
        self.client.connect(self.host, username=self.username, pkey=pkey)

    def exec(self, cmd):
        return super().exec(cmd)


class SshSession:
    """
    Class object to SSH with ssh key
    """

    def __init__(self, config):
        self.conf = config

    def get_ssh_session(self):
        """
        Creates an ssh object and returns that for further ssh execution
        @rtype: ssh Object
        """
        cfg = (
            read_config_file(self.conf)
            if self.conf
            else read_config_file(CONFIG_DEFAULTS["file"])
        )
        ssh_session = (
            SshBasic(cfg["workbench"])
            if cfg["auth"]["basic_auth"]
            else SshKeyBase(cfg["workbench"])
        )
        ssh_session.connect()
        return cfg, ssh_session
