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

from encrypted_settings.crypter import Crypter

__all___ = [
    'EncryptedConfig',
    'set_values'
]


class EncryptedConfig(object):
    """
    """
    def __init__(self, keyset_path, encrypted_settings_module):
        self._crypter = Crypter(keyset_path=keyset_path)
        self._encrypted_settings_module = encrypted_settings_module
        self._settings_module = __import__(encrypted_settings_module,
                                           fromlist=['.'])

    def __getattr__(self, key):
        ciphertext = getattr(self._settings_module, key, None)

        if ciphertext is None:
            raise KeyError(key)

        plaintext = self._crypter.decrypt(ciphertext)
        return plaintext


def set_values(keyset_path, encrypted_settings_module, module, keys):
    config = EncryptedConfig(keyset_path, encrypted_settings_module)

    for key in keys:
        plaintext = getattr(config, key)
        setattr(module, key, plaintext)
