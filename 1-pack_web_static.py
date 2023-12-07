#!/usr/bin/python3
# Compress before sending

from fabric.api import local
from datetime import datetime
import os.path

def do_pack():
    """
    Generate a .tgz archive from the contents of web_static folder
    """
    dt = datetime.utcnow()
    archive_name = "web_static_{}{}{}{}{}{}.tgz".format(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
    archive_path = "versions/{}".format(archive_name)

    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -czvf {} web_static".format(archive_path)).failed is True:
        return None
    return archive_path
