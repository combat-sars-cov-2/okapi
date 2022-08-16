import paramiko


class Ssh:
    """
    Class object to ssh to remote machine
    """

    def __init__(self, config):
        """
        Initialisation of the class attributes
        """
        self.username = config['username']
        self.host = config['domain']
        self.client = paramiko.client.SSHClient()

    def exec(self, cmd):
        """
        Execute a remote command
        :param cmd:
        :return:
        """
        stdin, stdout, stderr = self.client.exec_command(cmd)
        return stdout.read().decode()

    def close(self):
        """
        Close the ssh session
        :return:
        """
        self.client.close()


class SshBasic(Ssh):
    """
    Class object to SSH with username and password
    """

    def __init__(self, config):
        self.password = config['password']
        super().__init__(config)

    def connect(self):
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(self.host, username=self.username, password=self.password, look_for_keys=False,
                            allow_agent=False)

    def exec(self, cmd):
        return super().exec(cmd)


class SshKeyBase(Ssh):
    """
    Class object to SSH with ssh key
    """

    def __init__(self, config):
        self.username = config['username']
        self.host = config['domain']
        self.ssh_key = config['ssh_key_file']
        super().__init__()

    def connect(self):
        """Connect with the ssh key"""
        pkey = paramiko.RSAKey.from_private_key_file(self.ssh_key)
        policy = paramiko.AutoAddPolicy()
        self.client.set_missing_host_key_policy(policy)
        self.client.connect(self.host, username=self.username, pkey=pkey)
