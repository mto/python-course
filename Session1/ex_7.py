def filter(l, rex):
    ret = list()
    for x in l:
        if x.startswith(rex):
            ret.append(l)

filter(['aabc', 'aab', 'def'], 'a')