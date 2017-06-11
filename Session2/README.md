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

### 1.3 Vòng lặp *while* trong Python

```python
while CONDITION_CHECK:
      ...
```

Để đọc stdin gắn với file gồm nhiều dòng ta dùng vòng lặp *while*

```
line = input()
while line != '':
      ...
      line = input()
```


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
python ex_3.py eminfo.txt
```

## 2. Đọc & ghi file

Thực thi các đoạn mã sau

* Đọc nội dung file *meminfo.txt*
```python
f = open('./meminfo.txt', mode='r')
s = f.read()
print(s)
```

* Ghi ra file *out.txt*
```python
dst = open('./out.txt', mode='w')
dst.write('Blah blah')
```

* Kiểm tra *kiểu* giá trị trả về của hàm *open*

```python
f = open('./meminfo.txt', mode='r')
print(type(f))
```

### 2.1 Method *open* trong Python

https://docs.python.org/3/library/functions.html#open

```python
open(file[, mode[, buffering[, encoding[, errors]]]])
```

![](https://raw.githubusercontent.com/mto/python-course/master/Session2/material/builtin_methods.png)


Nằm trong nhóm *builtin* methods và đóng vai trò căn bản trong việc đọc/ghi file trên Python

__**Bài tập 4:**__

*Đọc nội dung file meminfo.txt và in ra màn hình các dòng có chứa chuỗi 'Total:' hoặc 'Free:'*

__Chú ý:__

Để làm bài tập 4 ta cần dùng vòng lặp *while* tương tự như ở bài tập 3 và method *readline* trên *file_object*

https://docs.python.org/3.6/library/io.html#io.IOBase


__**Bài tập 5:**__

![](https://raw.githubusercontent.com/mto/python-course/master/Session2/material/sm_admin_logo.png)

*Đọc nội dung file [logo.txt](https://raw.githubusercontent.com/mto/python-course/master/Session2/logo.txt) và in ra màn hình*

__**Bài tập 6:**__

*Đọc nội dung file [hanmactu.txt](https://raw.githubusercontent.com/mto/python-course/master/Session2/hanmactu.txt) và ghi mỗi khổ thơ ra 1 file riêng*


__**Bài tập 7:**__

*Tạo file ex_7.py có implement method 'tokenize' nhận đầu vào là file name và trả về list các từ trong file*

```python
def tokenize(fname):
    ret = list()
    ...
    return ret


print(tokenize('./hanmactu.txt'))
```

### 2.2 Wanna Cry

![](https://raw.githubusercontent.com/mto/python-course/master/Session2/material/wanna_cry.jpg)

Với các kiến thức đọc & ghi file hiện tại, ta có thể tạo một chương trình mô phỏng nguyên tắc hoạt động của virus Wanna Cry

__**Bài tập 8:**__

*Tạo file ex_8.py implement các method 'encrypt' và 'decrypt', tải file [wanna_cry.py](https://raw.githubusercontent.com/mto/python-course/master/Session2/wanna_cry.py) và thư mục [test_wanna_cry]() về cùng thư mục chứa ex_8.py và chạy file wanna_cry.py*


```python

'''
Method encrypt sửa nội dung file 'src' bằng cách thêm chuỗi 'code' vào đầu mỗi dòng
'''
def encrypt(src, code):
    ...


def decrypt(src, code, paid=False):
    if not paid:
       return 'Mời bạn trả tiền đã'
    se:
       # Khôi phục nội dung file ban đầu
```