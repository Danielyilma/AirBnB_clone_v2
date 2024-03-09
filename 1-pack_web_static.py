#!/usr/bin/python3
from fabric.api import *
from datetime import datetime
import os


def do_pack():
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
