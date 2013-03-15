#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Installs dependencies appropriate for the Python version."""
import subprocess
import sys

subprocess.call(["pip", "install", "--use-mirrors", "-r", "requirements.txt"])
if sys.version_info[0] >= 3: # Python 3
    # No Python 3-specific dependencies right now
    pass
else:  # Python 2
    subprocess.call(["pip", "install", "--use-mirrors", "unittest2"])
