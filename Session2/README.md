* Input & Output
* Đọc & ghi file

## 1. Input & Output

![](https://raw.githubusercontent.com/mto/python-course/master/Session2/material/meat_grinder.jpg)

Tải file [bootstrap.py](https://raw.githubusercontent.com/mto/python-course/master/Session2/bootstrap.py)

```python
host = input('Enter a valid domain:\n')
port = input('Enter a port number:\n')

print('Server started on %s:%s' % (host, port))
```

và [server.config](https://rawgithubusercontent.com/mto/python-course/master/Session2/server.config)

```config
'192.168.1.200'
5000
```

rồi chạy lần lượt các command sau đây trên cửa sổ **cmd**


```shell
python bootstrap.py

python bootstrap.py < server.config

python bootstrap.py < server.config > out.txt

python bootstrap.py > out.txt
```

Bất kỳ chương trình chạy trên máy tính nào cũng bao gồm:

**INPUT -> LOGIC_PROCESSING -> OUTPUT**

Ví dụ:

| Chương trình | Input | Output |
|---|---|---|
|Chrome Browser |User Preferences & actions | Windows rendering web content|
|Mine Sweeper game| Mouse clicks | Win/Game Over|
|OpenStack API| HTTP requests| Update on VPS status|
|WinRAR| List of files| Compressed .rar file|

### 1.1 stdin/stdout qua ví dụ mẫu

* stdin gắn với input của người dùng từ console
```shell
python bootstrap.py
```

* stdin gắn với input từ file cấu hình
```
python bootstrap.py < server.config
```

* stdout gắn với console
```
python bootstrap.py
```

* stdout gắn với file
```python
python bootstrap.py > out.
```

### 1.2 Method *input* trong Python

https://docs.python.org/3/library/functions.html#input

__Chú ý:__

Method *input* được định nghĩa trong *builtins* module của Python nên việc sử dụng không đòi hỏi *import* statement nào

__**Bài tập 1:**__

*Tạo file ex_1.py khi chạy lên sẽ prompt ra màn hình yêu cầu 'Nhập vào số N:' cho phép người dùng nhập vào giá trị của N, sau đó in ra stdout các số nguyên có 2 chữ số không vượt quá N*

__**Bài tập 2:**__

*Tạo file ex_2.py nhận input là output của câu lệnh 'dir' (trên Windows) hoặc 'ls -l' (trên Linux/Mac) và in ra màn hình toàn bộ input*

__Chú ý:__

Để chạy bài tập 2 ta dùng

```shell
dir > list_file_out.txt hoặc  ls -l > list_file_out.txt

python ex_2.py < list_file_out.txt
```

__**Bài tập 3:**__

*Tạo file ex_3.py nhận stdin là file [meminfo.txt](https://raw.githubusercontent.com/mto/python-course/master/Session2/meminfo.txt) và in ra màn hình toàn bộ nội dung của input file*

__Chú ý:__

Để chạy bài tập 3 ta cần download file meminfo về cùng thư mục với ex_3.py và chạy từ **cmd** với lệnh

```shell
python ex_3.py < meminfo.txt
```

## 2. Đọc & ghi file


