from __future__ import annotations


def launch(cfg, ssh_session):
    """
    launch irida-workbench instance
    \f
    """
    cmd = f"cd {cfg['root_path']};"
    cmd += "docker-compose -f docker-compose.irida-workbench.yml -f docker-compose.irida_ssl.yml up -d"
    ssh_session.exec(cmd)


def shut(cfg, ssh_session):
    """
    Shut irida-workbench instance
    \f
    """

    cmd = f"cd {cfg['root_path']};"
    cmd += (
        "docker-compose stop irida-workbench;"
    )
    ssh_session.exec(cmd)
