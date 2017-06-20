import base64

fr = open('./maria_ozawa_b64.txt', mode='rb')
fw = open('./maria_ozawa_b64_decoded.jpg', mode='wb')

fw.write(base64.b64decode(fr.read()))
