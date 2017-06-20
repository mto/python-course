import hashlib


def md5_checksum(fn):
    m = hashlib.md5()
    m.update(open(fn, mode='rb').read())

    return m.hexdigest()


cks1 = md5_checksum('./maria_ozawa.jpg')
cks2 = md5_checksum('./maria_ozawa_bis.jpg')
print(cks1)
print(cks2)
print(cks1 == cks2)
