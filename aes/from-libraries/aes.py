# Pour ce TP utiliser la bibliothèque pycryptodome
# https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html#classic-cipher-modes

import json
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes