from __future__ import annotations


def launch(cfg, ssh_session):
    """
    manage irida_workbench instance
    \f
    """
    cmd = f"cd {cfg['root_path']};"
    cmd += "docker-compose -f docker-compose.irida.yml -f docker-compose.irida_ssl.yml up -d"
    ssh_session.exec(cmd)


def shut(cfg, ssh_session):
    """
    Shut irida_workbench instance
    \f
    """

    cmd = f"cd {cfg['root_path']};"
    cmd += (
        "docker-compose stop irida_web;"
    )
    ssh_session.exec(cmd)
