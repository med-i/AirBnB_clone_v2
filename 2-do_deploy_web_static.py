#!/usr/bin/python3
"""
This module defines a script that distributes the archive web servers.
"""

from fabric.api import env, put, sudo

env.user = "ubuntu"
env.hosts = ["18.208.120.95", "52.207.131.83"]
env.key_filename = "/home/med/.ssh/id_rsa"


def do_deploy(archive_path):
    file_name = archive_path.split("/")[-1]
    base_dir = file_name.split(".")[0]
    release_path = f"/data/web_static/releases/{base_dir}/"
    web_static_path = f"{release_path}web_static/"

    put(archive_path, f"/tmp/{file_name}")
    sudo(f"mkdir -p {release_path}")
    sudo(f"tar -xzf /tmp/{file_name} -C {release_path}")
    sudo(f"rm /tmp/{file_name}")
    sudo(f"rsync -a {web_static_path} {release_path}")
    sudo(f"rm -rf {web_static_path}")
    sudo("rm -rf /data/web_static/current")
    sudo(f"ln -s {release_path} /data/web_static/current")

    print("New version deployed successfully!")
