f = open('hanmactu.txt')
dst = open('out.txt','w')

line = f.readline()

while line != '':
    dst.write(line)
    line = f.readline()