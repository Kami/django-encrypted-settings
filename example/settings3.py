"""
Method 3 - Automatically decrypt values and set attributes on the current
module.
"""

import sys

from encrypted_settings.config import set_values

KEYSET_PATH = '/my/path/to/keyczar_keyset'
ENCRYPTED_SETTINGS_MODULE = 'myapp.configs.encrypted_settings'

FACEBOOK_API_KEY = None

set_values(KEYSET_PATH, ENCRYPTED_SETTINGS_MODULE,
           sys.modules[__name__], ['FACEBOOK_API_KEY'])
