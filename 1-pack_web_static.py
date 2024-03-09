#!/usr/bin/python3
"""
The function `do_pack` creates a compressed archive of the 'web_static'
folder with a timestamp in the filename.
"""
from fabric.api import *
from datetime import datetime
import os


def do_pack():
    """
    The function `do_pack` creates a compressed archive of a specified
    directory and saves it in a 'versions' folder.
    """
    if not os.path.exists('versions'):
        os.mkdir('versions')

    created = datetime.now()
    archiveName = 'web_static_{}{}{}{}{}{}.tgz'.format(
        created.year, created.month,
        created.day, created.hour,
        created.minute, str(created.second)
    )

    local("tar -cvzf versions/{} web_static".format(archiveName))

    if os.path.exists('versions/{}'.format(archiveName)):
        return 'versions/{}'.format(archiveName)
    else:
        return None
