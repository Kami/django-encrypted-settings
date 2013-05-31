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
from os.path import join as pjoin
import unittest2 as unittest

from mock import Mock

from encrypted_settings.crypter import Crypter
from encrypted_settings.config import EncryptedConfig
from encrypted_settings.config import set_values

from fixtures import encrypted_settings

CWD = os.path.dirname(__file__)
KEYSET_PATH = os.path.realpath(pjoin(CWD, 'fixtures/keyset'))
ENCRYPTED_SETTINGS_MODULES = 'fixtures.encrypted_settings'


SETTING_NAME_TO_DECRYPTED_VALUE_MAP = {
    'MY_SECRET_KEY1': 'poniesrox1',
    'MY_SECRET_KEY2': 'poniesrox2',
    'MY_SECRET_KEY3': 'poniesrox3'
}


class CrypterTestCase(unittest.TestCase):
    def test_basic_functionality(self):
        crypter = Crypter(KEYSET_PATH)

        for key, expected in SETTING_NAME_TO_DECRYPTED_VALUE_MAP.items():
            value = getattr(encrypted_settings, key)
            plaintext = crypter.decrypt(value)
            self.assertEqual(plaintext, expected)


class EncryptedConfigTestCase(unittest.TestCase):
    def test_invalid_keys(self):
        config = EncryptedConfig(KEYSET_PATH, ENCRYPTED_SETTINGS_MODULES)
        self.assertRaises(KeyError, lambda: config.INVALID)
        self.assertRaises(KeyError, lambda: config.INVALID2)

    def test_valid_keys(self):
        config = EncryptedConfig(KEYSET_PATH, ENCRYPTED_SETTINGS_MODULES)

        for key, expected in SETTING_NAME_TO_DECRYPTED_VALUE_MAP.items():
            plaintext = getattr(config, key)
            self.assertEqual(plaintext, expected)


class TestSetValues(unittest.TestCase):
    def test_set_values_invalid_key(self):
        module = Mock()

        self.assertRaises(KeyError, set_values, KEYSET_PATH,
                          ENCRYPTED_SETTINGS_MODULES, module,
                          ['MY_SECRET_KEY1', 'INVALID'])

    def test_set_values_1(self):
        module = Mock()

        self.assertTrue(isinstance(module.MY_SECRET_KEY1, Mock))

        set_values(KEYSET_PATH, ENCRYPTED_SETTINGS_MODULES, module,
                   ['MY_SECRET_KEY1', 'MY_SECRET_KEY3'])

        self.assertEqual(module.MY_SECRET_KEY1, 'poniesrox1')
        self.assertEqual(module.MY_SECRET_KEY3, 'poniesrox3')

    def test_set_values_2(self):
        module = Mock()

        self.assertTrue(isinstance(module.MY_SECRET_KEY1, Mock))
        self.assertTrue(isinstance(module.MY_SECRET_KEY2, Mock))
        self.assertTrue(isinstance(module.MY_SECRET_KEY3, Mock))

        set_values(KEYSET_PATH, ENCRYPTED_SETTINGS_MODULES, module,
                   SETTING_NAME_TO_DECRYPTED_VALUE_MAP.keys())

        for key, expected in SETTING_NAME_TO_DECRYPTED_VALUE_MAP.items():
            actual = getattr(module, key)
            self.assertEqual(actual, expected)


if __name__ == '__main__':
    sys.exit(unittest.main())
