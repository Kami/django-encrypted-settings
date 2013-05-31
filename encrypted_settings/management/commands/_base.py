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

from keyczar import keyczar
from django.core.management.base import BaseCommand, CommandError

__all__ = [
    'BaseAppCommand'
]


class BaseAppCommand(BaseCommand):
    def __init__(self, *args, **kwargs):
        super(BaseAppCommand, self).__init__(*args, **kwargs)

    def validate_args(self, args):
        if len(args) != 1:
            raise CommandError('Missing required keyset path argument')

        keyset_path = args[0]

        if not os.path.exists(keyset_path):
            raise CommandError('Directory "%s" doesn\'t exist' % (keyset_path))

        return args

    def get_crypter(self, args):
        args = self.validate_args(args)
        keyset_path = args[0]
        crypter = keyczar.Crypter.Read(keyset_path)
        return crypter
