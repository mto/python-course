import os

home = 'C:\\Users\\' + os.getlogin() if os.name == 'nt' else '/home/' + os.getlogin()

for envk in ['HOME', 'HOME_PATH']:
    if os.environ.get(envk) is not None:
        home = os.environ.get(envk)
        break

print(os.listdir(home))
