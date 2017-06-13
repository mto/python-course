def tokenize(fname):
    ret = list()

    f = open(fname, mode='r', encoding='utf-8')
    line = f.readline()
    while line != '':
        if line != '\n':
            ret.extend(line.strip('\n').split(' '))
        line = f.readline()

    return ret


print(tokenize('./hanmactu.txt'))
