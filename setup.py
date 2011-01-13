#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
liu-anslagstavlan
-----------------

Unoffical library for working with the bulletin board of Linköping University.
Read-only, uses `httplib2` internally if available.

"""
from setuptools import setup

setup(
    name='liu-anslagstavlan',
    version='0.9.0',
    url='http://github.com/pilt/liu-anslagstavlan',
    license='BSD',
    author='Simon Pantzare',
    author_email='simon@pewpewlabs.com',
    description='Unoffical library for working with the bulletin board of Linköping University.',
    long_description=__doc__,
    packages=[
        'liuanslagstavlan',
    ],
    namespace_packages=['liuanslagstavlan'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'setuptools',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
