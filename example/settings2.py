"""
Method 2 - Passing a path to a Python module which contains encrypted settings.
"""

from encrypted_settings.config import EncryptedConfig

config = EncryptedConfig('/my/path/to/keyczar_keyset', 'myapp.configs.encrypted_settings')

FACEBOOK_API_KEY = config.FACEBOOK_API_KEY
