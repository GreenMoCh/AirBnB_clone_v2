#!/usr/bin/python3
""" Deploy archive """

from fabric.api import local, env, put, run
from datetime import datetime
from os.path import exists

env.hosts = ['54.157.168.41', '54.242.203.200']


def do_pack():
    """
    Generate a .tgz from the contents of the web_satatic folder
    """
    dt = datetime.utcnow()
    archive_name = "web_static_{}{}{}{}{}{}.tgz".format(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
    archive_path = "versions/{}".format(archive_name)

    if exists("versions") is False:
        local("mkdir -p versions")

    if local("tar -czvf {} web_static".format(archive_path)).failed is True:
        return None
    return archive_path

def do_deploy(archive_path):
    """
    Distributes an archive to the web servers
    """
    if not exists(archive_path):
        return False

    try:
        archive_name = archive_path.split("/")[-1]
        archive_no_ext = archive_name.split(".")[0]

        put(archive_path, '/tmp/{}'.format(archive_name))
        run('mkdir -p /data/web_static/releases/{}/'.format(archive_name, archive_no_ext))
        run('rm /tmp/{}'.foramt(archive_name))
        run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/'.format(archive_no_ext, archive_no_ext))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(archive_no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.foramt(archive_no_ext))
        return True
    except Exception as e:
        print(e)
        return False

def deploy():
    """
    Creates an archive to the web servers
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
