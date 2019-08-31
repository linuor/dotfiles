#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import configparser
import os, os.path
import subprocess

pkg_dir = os.path.dirname(__file__)
conf = configparser.ConfigParser()
default_ini = open(pkg_dir + "/default.ini")
conf.read_file(default_ini)
local_ini = open(pkg_dir + "/local.ini")
conf.read_file(local_ini)
subprocess.run(["git", "config", "--global", "user.name",\
        conf["git"]["username"]], check=True)
subprocess.run(["git", "config", "--global", "user.email",\
        conf["git"]["email"]], check=True)
subprocess.run(["git", "config", "--global", "core.excludesfile",\
        pkg_dir + "/git/global.gitignore"], check=True)

close(local_ini)
close(default_ini)

