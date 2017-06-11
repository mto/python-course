* Input & Output
* Đọc & ghi file

## 1. Input & Output

![](https://raw.githubusercontent.com/mto/python-course/master/Session2/material/meat_grinder.jpg)

Tải file [bootstrap.py](https://raw.githubusercontent.com/mto/python-course/master/Session2/bootstrap.py) và [server.config](https://rawgithubusercontent.com/mto/python-course/master/Session2/server.config)
rồi chạy lần lượt các command sau đây trên cửa sổ **cmd**

```python
host = input('Enter a valid domain:\n')
port = input('Enter a port number:\n')

print('Server started on %s:%s' % (host, port))
```

```shell
python bootstrap.py

python bootstrap.py < server.config

python bootstrap.py < server.config > out.txt

python bootstrap.py > out.txt
```

## 2. Đọc & ghi file


