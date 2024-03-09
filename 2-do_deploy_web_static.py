#!/usr/bin/python3

from fabric.api import env, put, run, sudo
import os
from sys import argv

env.hosts = ['54.237.124.13', '34.207.120.149']
    

def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False
    filename = archive_path[9:archive_path.index('.')]
    try:
        put(archive_path, '/tmp/')
        run(f'mkdir -p /data/web_static/releases/{filename}')
        run(f'tar -xzf /tmp{archive_path[8:]} -C /data/web_static/releases/{filename}')
        run(f'rm /tmp{archive_path[8:]}')
        run(f'mv /data/web_static/releases/{filename}/web_static/* /data/web_static/releases/{filename}/')
        run(f'rm -rf /data/web_static/releases/{filename}/web_static')
        run('rm -rf /data/web_static/current')
        run(f'ln -s /data/web_static/releases/{filename}\
 /data/web_static/current')
    except Exception as f:
        return False
    return True
    