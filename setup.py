#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from os.path import join, dirname


def read(fname):
    return open(join(dirname(__file__), fname)).read()

PKG = 'SimpleConfigParser'
VERSION = '0.1.0'

setup(
    name=PKG,
    version=VERSION,
    description="Simplifies and enchances functionalities in Python's ConfigParser",
    long_description=read('README'),
    author="Helgi Þorbjörnsson",
    author_email="helgi@php.net",
    url="http://github.com/helgi/python-simpleconfigparser",
    packages=find_packages(),
    install_requires=[],
    license="MIT License",
    keywords="ConfiParser,ini",
    zip_safe=True,
    test_suite="tests",
    tests_require=[],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ]
)
