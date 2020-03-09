#!/usr/bin/python3

from speck import SpeckCipher

plaintext = 0x6c617669757165207469206564616d20
key = 0x0f0e0d0c0b0a09080706050403020100

# make a cipher 
cipher = SpeckCipher(key)

# encrypt"
ciphertext = cipher.encrypt(plaintext)

# decrypt"
plaintext_2nd = cipher.decrypt(ciphertext)

# show result
print("key: 0x" + hex(cipher.key))
print("PT: 0x" + hex(plaintext))
print("CT: 0x" + hex(ciphertext))
print("decrypted PT: 0x" + hex(plaintext_2nd))

# verify that the decrypted message is equal
#   to the original message
if plaintext_2nd == plaintext:
  print("verify ok")
else:
  print("verify NOT ok")