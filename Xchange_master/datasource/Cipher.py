from pyDes import *

Des_Key = "BHC#@*UM" 
Des_IV = '\0\1\2\3\4\5\6\7'
encoder = des(Des_Key, CBC, Des_IV, pad=None, padmode=PAD_PKCS5)


def encode(source):
    return encoder.encrypt(source)


def decode(source):
    return encoder.decrypt(source)
