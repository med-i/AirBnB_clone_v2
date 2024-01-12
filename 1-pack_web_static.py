#!/usr/bin/python3
"""
This module defines a script to pack web_static.
"""

import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """
    source_dir = "web_static"
    output_dir = "versions"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    time_str = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"{source_dir}_{time_str}.tgz"
    archive_path = os.path.join(output_dir, archive_name)

    try:
        return local(f"tar -czvf {archive_path} {source_dir}")
    except Exception as e:
        print(f"An error code occured: {e}")
        return None
