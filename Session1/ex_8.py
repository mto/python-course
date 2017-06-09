import os

for x in os.listdir('.'):
    if x.endswith('.py'):
        print(x)