f = open('./logo.txt', mode='r')
line = f.readline()

while line != '':
    print(line, end='')
    line = f.readline()
