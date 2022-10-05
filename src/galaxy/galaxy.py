from __future__ import annotations


def launch(cfg, ssh_session):
    """
    manage galaxy_workbench instance
    \f
    """
    cmd = f"cd {cfg['root_path']};"
    cmd += "docker-compose -f docker-compose.yml -f docker-compose.singularity.yml up -d"
    ssh_session.exec(cmd)


def shut(cfg, ssh_session):
    """
    Shut galaxy_workbench instance
    \f
    """

    cmd = f"cd {cfg['root_path']};"
    cmd += (
        "docker-compose stop galaxy_workbench-server;"
    )
    ssh_session.exec(cmd)
