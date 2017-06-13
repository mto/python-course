f = open('./hanmactu.txt', mode='r', encoding='utf-8')

idx = 1
tmpf = open('./out_' + str(idx) + '.txt', mode='w', encoding='utf-8')
line = f.readline()

while line != '':
    if line == '\n':
        idx += 1
        tmpf = open('./out_' + str(idx) + '.txt', mode='w', encoding='utf-8')
    else:
        tmpf.write(line)

    line = f.readline()
