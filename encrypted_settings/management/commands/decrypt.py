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

from _base import BaseAppCommand

__all__ = [
    'Command'
]


class Command(BaseAppCommand):
    args = '<keyczar keyset path>'
    help = 'Decrypt a ciphertext using a primary key from the keyczar keyset'

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

    def handle(self, *args, **options):
        crypter = self.get_crypter(args)
        ciphertext = raw_input('Enter ciphertext to decrypt: ')
        plaintext = crypter.Decrypt(ciphertext)

        self.stdout.write(plaintext)
