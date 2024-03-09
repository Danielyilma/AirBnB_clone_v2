#!/usr/bin/python3
"""
The Python script contains functions for creating a compressed archive of
a directory, deploying it to a remote server, and creating symbolic links
for the deployment.
"""
from fabric.api import env, put, run, sudo, local
from datetime import datetime
import os

env.hosts = ['54.237.124.13', '34.207.120.149']


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


def do_deploy(archive_path):
    '''This Python function `do_deploy` is designed to deploy a
    compressed archive to a remote server and create symbolic links
    for the current deployment. Here is a breakdown of what the code is
     doing'''
    if not os.path.exists(archive_path):
        return False
    filename = archive_path[9:archive_path.index('.')]
    try:
        put(archive_path, '/tmp/')
        run(f'mkdir -p /data/web_static/releases/{filename}')
        run(f'tar -xzf /tmp{archive_path[8:]} -C /data/web_static/\
releases/{filename}')
        run(f'rm /tmp{archive_path[8:]}')
        run(f'mv /data/web_static/releases/{filename}/web_static/*\
 /data/web_static/releases/{filename}/')
        run(f'rm -rf /data/web_static/releases/{filename}/web_static')
        run('rm -rf /data/web_static/current')
        run(f'ln -s /data/web_static/releases/{filename}\
 /data/web_static/current')
    except Exception as f:
        return False
    return True


def deploy():
    '''distributing the archive and deploying the web static fils'''
    archive_name = do_pack()
    if not archive_name:
        return False
    return do_deploy(archive_name)
