import re

rex = '[0-9]+\,[0-9]+'

pattern = re.compile(rex)

print(pattern.findall(open('./evnexpress.txt', mode='r').read()))
