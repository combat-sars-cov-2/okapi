from __future__ import annotations


def start(self):
    """
    start irida instance
    \f
    """
    cmd = "docker-compose start irida_web"
    pass


def stop(self):
    """
    Stop irida instance
    \f
    """
    cmd = "docker-compose stop irida_web"
