#!/usr/bin/env python
# Licensed to Tomaz Muraus under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# Tomaz muraus licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys
import unittest

unittest

from os.path import join as pjoin

from distutils.core import Command
from setuptools import setup, find_packages
from subprocess import call

CWD = os.path.dirname(os.path.abspath((__file__)))
TESTS_PATH = pjoin(CWD, 'tests/')

sys.path.insert(0, CWD)


def read_version_string():
    version = None
    sys.path.insert(0, os.path.join(os.getcwd()))
    from encrypted_settings import __version__
    version = __version__
    sys.path.pop(0)
    return version


# Commands based on Libcloud setup.py:
# https://github.com/apache/libcloud/blob/trunk/setup.py
class Flake8Command(Command):
    description = 'Run flake8 script'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            import flake8
            flake8
        except ImportError:
            print ('Missing "flake8" library. You can install it using pip: '
                   'pip install flake8')
            sys.exit(1)

        cwd = os.getcwd()
        retcode = call(('flake8 %s/encrypted_settings/ %s/tests/tests.py' %
                       (cwd, cwd)).split(' '))
        sys.exit(retcode)


class TestCommand(Command):
    description = 'Run test test script'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            import unittest2
            unittest = unittest2
        except ImportError:
            print ('Missing "unittest2" library. You can install it using '
                   'pip: pip install unittest2')
            sys.exit(1)

        loader = unittest.TestLoader()
        tests = loader.discover(TESTS_PATH)
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(tests)

        if not result.wasSuccessful():
            sys.exit(1)


setup(
    name='django-encrypted-settings',
    version=read_version_string(),
    description='Thin wrapper around Python keyczar bindings which allows ' +
                'you to manage and use encrypted settings in your Django app.',
    author='Tomaz Muraus',
    author_email='tomaz@tomaz.me',
    url='https://github.com/Kami/django-encrypted-settings',
    classifiers=['Development Status :: 2 - Pre-Alpha',
                 'License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2.6',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: Implementation :: PyPy',
                 'Environment :: Console',
                 ],
    cmdclass={
        'test': TestCommand,
        'flake8': Flake8Command
    },
    platforms=['Any'],
    install_requires=[
        'python-keyczar',
    ],
    packages=find_packages(),
    package_dir={
        'encrypted_settings': 'encrypted_settings'
    },
)
