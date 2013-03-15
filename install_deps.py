#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Installs dependencies appropriate for the Python version."""
import subprocess
import sys

subprocess.call(["pip", "install", "--use-mirrors", "-r", "requirements.txt"])
if sys.version_info[0] >= 3: # Python 3
    subprocess.call(["pip", "install", "--use-mirrors", "unittest2py3k"])
else:  # Python 2
    subprocess.call(["pip", "install", "--use-mirrors", "unittest2"])
