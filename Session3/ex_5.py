fr = open('./maria_ozawa.jpg', mode='rb')
fw = open('./maria_ozawa_bis.jpg', mode='wb')

fw.write(fr.read())
