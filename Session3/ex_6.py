import base64

fr = open('./maria_ozawa.jpg', mode='rb')
fw = open('./maria_ozawa_b64.txt', mode='wb')

fw.write(base64.b64encode(fr.read()))
