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

import os.path

try:
    from keyczar import keyczar
except ImportError:
    raise ImportError('Missing keyczar dependency. You can install it ' +
                      'using pip: pip install python-keyczar')


__all___ = [
    'Crypter',
]


class Crypter(object):
    """
    Currently a simple wrapper around keyczar. Eventually the plan is to
    support more backends.
    """

    def __init__(self, keyset_path):
        if not os.path.exists(keyset_path):
            raise ValueError('keyset_path directory doesn\'t exist')

        self._keyset_path = keyset_path
        self._crypter = keyczar.Crypter.Read(self._keyset_path)

    def decrypt(self, ciphertext):
        plaintext = self._crypter.Decrypt(ciphertext)
        return plaintext

    def encrypt(self, plaintext):
        ciphertext = self._crypter.Encrypt(plaintext)
        return ciphertext
