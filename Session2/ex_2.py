try:
    s = input()
    while True:
        print(s)
        s = input()
except EOFError as ex:
    pass
