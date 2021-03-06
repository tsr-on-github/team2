# crypto class

import base64
import random
import string
from Crypto import Random
from Crypto.Cipher import AES

def genKey():
    return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(50)])

class AESCipher(object):
    def __init__(self, key, block_size=32):
        self.bs = block_size
        if len(key) >= len(str(block_size)):
            self.key = key[:block_size]
        else:
            self.key = self._pad(key)

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:]))

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    def _unpad(self, s):
        return s[:-ord(s[len(s)-1:])]


if __name__ == '__main__':
    key = genKey()
    text = 'B IS VERY BAD\nDDDDDDDDDD'
    print('key: ' + key)
    print('txt: ' + text + '\n')
    b = AESCipher(key)
    encoded = b.encrypt("hogehuga")
    printf('enc: ' + encoded)



# ref: https://qiita.com/teitei_tk/items/0b8bae99a8700452b718
# ref: https://github.com/teitei-tk/Simple-AES-Cipher