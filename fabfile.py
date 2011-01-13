# -*- coding: utf-8 -*-
import os
import sys

from fabric.api import *

env.hosts = ['localhost']
env.project_root = os.path.abspath(os.path.dirname(__file__))


def _envrun(command):
    return run('workon liu-anslagstavlan && ' + command)


def doc():
    """Regenerate Sphinx documentation."""
    with cd(env.project_root):
        _envrun('sphinx-build . ./html')


def test():
    """Run tests."""
    with cd(env.project_root):
        _envrun('python liuanslagstavlan/util.py')
        _envrun('python liuanslagstavlan/api.py')
        _envrun('python liuanslagstavlan/constants.py')
