"""
Method 1 - explicitly calling decrypt method with a ciphertext.
"""

from encrypted_settings.crypter import Crypter

crypter = Crypter('/my/path/to/keyczar_keyset')

FACEBOOK_API_KEY = crypter.decrypt('ciphertext')
