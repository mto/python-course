f = open('./meminfo.txt', mode='r')
line = f.readline()

while line != '':
    if 'Total:' in line or 'Free:' in line:
        print(line, end='')

    line = f.readline()
