from __future__ import annotations


def start(ssh_session):
    """
    start irida instance
    \f
    """
    cmd = "docker-compose start galaxy-server"
    ssh_session.exec(cmd)


def stop(ssh_session):
    """
    Stop irida instance
    \f
    """
    cmd = "docker-compose stop galaxy-server"
    ssh_session.exec(cmd)
