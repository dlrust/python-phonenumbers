#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='phonenumbers',
    version='4.7b1',
    description="Python version of Google's common library for parsing, formatting, storing and validating international phone numbers.",
    author='David Drysdale',
    author_email='dmd@lurklurk.org',
    url='https://github.com/daviddrysdale/python-phonenumbers',
    license='Apache License 2.0',
    package_dir = {'': 'python'},
    packages=['phonenumbers', 'phonenumbers.data', 'phonenumbers.geodata'],
    test_suite="tests",
    platforms='Posix; MacOS X; Windows',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Communications :: Telephony',
    ],
)
