from __future__ import annotations


def start(ssh_session):
    """
    start irida instance
    \f
    """
    cmd = "docker-compose start irida_web"
    ssh_session.exec(cmd)


def stop(ssh_session):
    """
    Stop irida instance
    \f
    """
    cmd = "docker-compose stop irida_web"
    ssh_session.exec(cmd)
